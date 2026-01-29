# Face Attendance System 

A simple **face recognition based attendance system** using **OpenCV (LBPH)**.  
This project captures faces from your webcam, recognizes them, and logs attendance automatically in a CSV file.

---

## 🔹 Features

- Real-time face recognition using **OpenCV LBPH algorithm**
- Attendance logging in `attendance.csv` with **timestamp**
- Marks **Unknown** for unregistered faces
- Beginner-friendly and **no heavy dependencies** like `dlib` or `face_recognition`
- Works on **Windows/Linux** with Python + OpenCV

---

## 🔹 Tech Stack

- **Python 3.x**
- **OpenCV**
- **NumPy**
- **CSV file handling** for attendance logging

---

## 🔹 How It Works

1. Train the model using faces of known students (outputs `model.yml` + `labels.npy`)
2. Run `recognize_face.py`
3. The camera opens and detects your face
4. If the face is recognized:
   - Name appears on screen
   - Attendance is recorded in `attendance.csv`
5. Press `q` to exit

---

## 🔹 Setup & Run

1. Install dependencies:

```bash
pip install opencv-python numpy
