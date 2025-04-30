from flask import Flask, render_template, jsonify, Response
from flask_cors import CORS
from threading import Thread, Lock
import cv2
from ultralytics import YOLO
import time
import base64

app = Flask(__name__)
CORS(app)

# YOLO modelini yükle
model = YOLO("yolov8s.pt")

# Video yolu
VIDEO_PATH = "library/video11.mp4"

# Masalar ve koordinatlar (x1, y1, x2, y2)
tables = {
    "Table 11": (346, 300, 534, 612),
    "Table 12": (542, 300, 758, 614),
    "Table 21": (1042, 340, 1252, 610),
    "Table 22": (1250, 340, 1442, 610)
}

# İzin verilen etiketler
allowed_labels = ['person', 'laptop', 'book', 'backpack', 'cell phone']

# Her masa için sayaçlar (object_only durumu için)
object_only_timers = {name: None for name in tables}

# Masa durumlarını saklayan sözlük
current_status = {name: {"status": "empty", "people": 0} for name in tables}

# Anlık video bilgisi
video_info = {"time": 0.0, "frame": ""}

# Paylaşılan veriler için kilit
status_lock = Lock()

@app.route("/")
def index():
    return render_template("HomePage.html")

@app.route("/api/status")
def get_status():
    with status_lock:
        return jsonify({
            "status": current_status,
            "time": round(video_info["time"], 2),
            "frame": video_info["frame"]
        })

def encode_frame_to_base64(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer).decode('utf-8')

def generate_video():
    cap = cv2.VideoCapture(VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_duration = 1 / fps
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("🔁 Video bitti, başa sarılıyor...")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            start_time = time.time()
            object_only_timers.update({name: None for name in tables})
            continue

        current_time = time.time() - start_time
        results = model.track(frame, persist=True, verbose=False)
        new_status = {}

        for name, (x1, y1, x2, y2) in tables.items():
            person_count = 0
            object_detected = False
            detected_objects = []

            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls_id = int(box.cls[0])
                    label = model.model.names[cls_id]
                    conf = float(box.conf[0])

                    if conf < 0.3 or label not in allowed_labels:
                        continue

                    xA, yA, xB, yB = map(int, box.xyxy[0])
                    center_x = (xA + xB) // 2
                    center_y = (yA + yB) // 2

                    if x1 <= center_x <= x2 and y1 <= center_y <= y2:
                        detected_objects.append(label)
                        if label == "person":
                            person_count += 1
                        else:
                            object_detected = True

            # Durum güncelleme
            if person_count > 0:
                new_status[name] = {"status": "occupied", "people": person_count}
                object_only_timers[name] = None
            elif object_detected:
                if object_only_timers[name] is None:
                    object_only_timers[name] = current_time

                elapsed = current_time - object_only_timers[name]
                if elapsed >= 20:
                    new_status[name] = {"status": "object_only", "people": 0}
                else:
                    new_status[name] = {"status": "empty", "people": 0}
            else:
                new_status[name] = {"status": "empty", "people": 0}
                object_only_timers[name] = None

            # Log
            print(f"[{current_time:.2f}s] {name} - {new_status[name]['status']} - "
                  f"People: {person_count}, Objects: {detected_objects}")

        # Global durumu güncelle
        with status_lock:
            global current_status
            current_status = new_status

        video_info["time"] = current_time
        video_info["frame"] = encode_frame_to_base64(frame)

        time.sleep(frame_duration)

    cap.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    def generate():
        cap = cv2.VideoCapture(VIDEO_PATH)
        if not cap.isOpened():
            print("❌ Video dosyasına erişilemiyor!")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("🔁 Video bitti, başa sarılıyor...")
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            try:
                _, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                print(f"❌ Frame işlenirken hata oluştu: {e}")
                break

        cap.release()

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

def start_video_thread():
    thread = Thread(target=generate_video)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    start_video_thread()
    app.run(debug=True)
