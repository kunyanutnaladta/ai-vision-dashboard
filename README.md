# 🚀 My AI Dashboard

<img width="1919" height="1124" alt="Screenshot 2026-05-05 165842" src="https://github.com/user-attachments/assets/e0939af0-8c06-4fd0-b09b-ae0afa337e7e" />

## 📌 Overview

My AI Dashboard คือโปรเจกต์ AI ที่รวม:

* 🎯 Object Detection (YOLO)
* 🧑 Face Recognition (InsightFace)

ไว้ในเว็บเดียว ใช้งานง่ายผ่าน browser

---

## ⚙️ Features

* 🎯 ตรวจจับวัตถุด้วย YOLO
* 🧑 ตรวจจับและจดจำใบหน้าด้วย InsightFace
* 🌐 Web UI ใช้งานผ่าน browser
* ⚡ รันง่ายในเครื่องเดียว
* 🧠 รองรับหลายโมเดล

---

## 🗂️ Project Structure

```bash
my-ai-dashboard/
│
├── app.py
├── index.html
├── requirements.txt
├── setup.bat
├── yolo11n.pt
├── yolo26n.pt
└── venv/
```

---

## 🛠️ Installation

### 1. Clone repo

```bash
git clone https://github.com/your-username/my-ai-dashboard.git
cd my-ai-dashboard
```

### 2. สร้าง virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python app.py
```

เปิด browser ไปที่:

```
http://localhost:5000
```

---

## 🧠 AI Models

### 🔍 YOLO (Object Detection)

* `yolo11n.pt`
* `yolo26n.pt`

### 🧑 InsightFace (Face Recognition)

* ตรวจจับใบหน้า
* สร้าง embedding
* เปรียบเทียบใบหน้า

---

## 💡 Future Improvements

* [ ] เพิ่มระบบบันทึกใบหน้า (Face Register)
* [ ] เพิ่มฐานข้อมูล (SQLite / Firebase)
* [ ] เพิ่ม UI เลือกโหมด YOLO / Face
* [ ] รองรับ GPU (CUDA)

---

## 🤝 Contributing

สามารถ fork และ pull request ได้

---

## 📄 License

MIT License

