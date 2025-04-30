## 📚 Table Occupancy Detection System | Masa Doluluk Tespit Sistemi

### 🔍 Description | Açıklama

**EN:**  
This project is a table occupancy detection system using **YOLOv8 object detection**. It analyzes a video feed from a fixed camera in a library-like environment to determine if tables are:

- ✅ Occupied (people present),
- ⚠️ Object-only (objects like books or laptops present but no person for 20+ seconds),
- 🟩 Empty (no people or objects detected).

The system visualizes table statuses on a web interface using **Flask**, **HTML**, and **JavaScript (AJAX)**.

---

**TR:**  
Bu proje, **YOLOv8 nesne tespiti** kullanarak masa doluluk durumlarını tespit eden bir sistemdir. Sabit bir kameradan gelen görüntüye dayanarak kütüphane benzeri bir ortamda masaların:

- ✅ Dolu (insan var),
- ⚠️ Sadece nesne var (kitap/laptop gibi nesne var ama 20+ saniyedir insan yok),
- 🟩 Boş (hiçbir insan veya nesne yok)

durumlarını analiz eder. Durumlar Flask, HTML ve JavaScript (AJAX) ile geliştirilen bir web arayüzünde gösterilir.

---

### 🧠 Technologies | Teknolojiler

- Python (Flask)
- OpenCV
- YOLOv8 (via Ultralytics)
- JavaScript (AJAX)
- HTML & CSS

---

### 🚀 Setup & Run | Kurulum ve Çalıştırma

**EN:**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/table-occupancy-detector.git
   cd table-occupancy-detector
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your video file at `library/video11.mp4`.

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser:
   ```
   http://localhost:5000
   ```

---

**TR:**

1. Depoyu klonla:
   ```bash
   git clone https://github.com/kullaniciadi/table-occupancy-detector.git
   cd table-occupancy-detector
   ```

2. Gerekli kütüphaneleri yükle:
   ```bash
   pip install -r requirements.txt
   ```

3. Video dosyanı `library/video11.mp4` yoluna yerleştir.

4. Uygulamayı başlat:
   ```bash
   python app.py
   ```

5. Tarayıcıdan eriş:
   ```
   http://localhost:5000
   ```

---

### 📂 Folder Structure | Klasör Yapısı

```
table-occupancy-detector/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── HomePage.html      # Web interface
├── static/
│   └── script.js          # JavaScript for AJAX & UI
├── library/
│   └── video11.mp4        # Input video (you provide)
```

---

### 📸 Table Statuses | Masa Durumları

- 🔴 **Occupied** – Person detected at table  
- 🟡 **Object Only** – No person, but objects detected for 20+ seconds  
- 🟢 **Empty** – No people or objects detected

---

### 📌 Notes | Notlar

- You can customize table coordinates in `app.py` under the `tables` dictionary.
- Object types include: `person`, `book`, `laptop`, `backpack`, `cell phone`.

---

### 📃 License | Lisans

MIT License
