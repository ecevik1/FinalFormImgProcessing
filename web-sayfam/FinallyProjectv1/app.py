from flask import Flask, render_template, jsonify
from flask_cors import CORS
from threading import Thread
import cv2
from ultralytics import YOLO
import time

app = Flask(__name__)
CORS(app)

current_status = {
    "Table 11": {"occupied": False, "people": 0},
    "Table 12": {"occupied": False, "people": 0},
    "Table 21": {"occupied": False, "people": 0},
    "Table 22": {"occupied": False, "people": 0}
}

model = YOLO("yolov8s.pt")

tables = {
    "Table 11": (346, 300, 534, 612),
    "Table 12": (542, 300, 758, 614),
    "Table 21": (1042, 340, 1252, 610),
    "Table 22": (1250, 340, 1442, 610)
}

allowed_labels = ['person', 'laptop', 'book', 'backpack', 'cell phone']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/status")
def get_status():
    return jsonify(current_status)

def video_loop():
    global current_status
    cap = cv2.VideoCapture("library/video11.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("🔁 Video bitti, başa sarılıyor...")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        results = model.track(frame, persist=True, verbose=False)
        new_status = {}

        for name, (x1, y1, x2, y2) in tables.items():
            is_occupied = False
            person_count = 0

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
                        if label == "person":
                            person_count += 1
                        is_occupied = True

            new_status[name] = {
                "occupied": is_occupied,
                "people": person_count
            }

        current_status = new_status

        time.sleep(0.5)

    cap.release()
    cv2.destroyAllWindows()

def start_video_thread():
    thread = Thread(target=video_loop)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    start_video_thread()
    app.run(debug=True)