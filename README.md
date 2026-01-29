# **Face Recognition Attendance System**

# 1. Project Overview

This project is a **real-time face recognition attendance system** that automatically logs punch-in and punch-out times using a webcam. It uses **OpenCV’s LBPH (Local Binary Patterns Histograms)** algorithm to identify registered users.

**Key Features:**

* User face registration via webcam
* Real-time recognition
* Automatic attendance logging
* Handles moderate lighting variations
* Basic spoof prevention (static photo detection)

---

# 2. Folder / File Structure

```
Face-Recognition-Attendance/
│
├── recognize_face.py       # Real-time recognition & attendance logging
├── register_face.py        # Capture images for new users
├── train.py                # Train the LBPH face recognition model
├── dataset/                # Sample images of registered users (5–10 per user)
├── README.md               # Project description & setup instructions
├── Face_Recognition_Attendance_Documentation.docx  # Detailed documentation
├── .gitignore              # Files to ignore (venv, models, logs)
```

**Note:** Dynamic/generated files like `attendance.csv`, `model.yml`, and `labels.npy` are **included in gitignore folder**.

---

# 3. Model and Approach

**Model Used:** LBPH (Local Binary Patterns Histograms) Face Recognizer
**Library:** OpenCV (`opencv-contrib-python`)

**Approach:**

1. **Face Registration:** Capture multiple facial images per user
2. **Training:** Process images with LBPH, assign labels, save `model.yml` and `labels.npy`
3. **Recognition:** Predict user label from live webcam feed using confidence threshold
4. **Attendance Logging:** Recognized users logged in `attendance.csv`

**Why LBPH:**

* Lightweight and real-time capable
* Works with small datasets
* Handles moderate lighting variations
* Beginner-friendly

---

# 4. Training Process

**Dataset Preparation:**

* Folder per user in `dataset/` with 5–20 images
* Include slight variations in angle/expression

**Training Steps:**

1. Run `train.py`
2. Script reads images, converts to grayscale
3. Assign numerical labels per user
4. Train LBPH recognizer
5. Save model and labels

**Usage:**

* Load model and labels in `recognize_face.py`
* Start webcam for recognition
* Attendance logged automatically

---

# 5. Setup Instructions

1. **Clone Repo:**

```bash
git clone https://github.com/Anshika-7-sys/Face-Recognition-Attendance.git
cd Face-Recognition-Attendance
```

2. **Install Dependencies:**

```bash
pip install opencv-contrib-python numpy
```

3. **Register Users:**

```bash
python register_face.py
```

* Capture 5–20 images per user

4. **Train Model:**

```bash
python train.py
```

5. **Run Real-Time Recognition & Attendance:**

```bash
python recognize_face.py
```

* Webcam opens, attendance logged automatically

---

# 6. Accuracy & Limitations

| Condition                 | Expected Accuracy |
| ------------------------- | ----------------- |
| Normal lighting           | 90–95%            |
| Moderate lighting changes | 80–90%            |
| Low/harsh lighting        | <80%              |

**Known Limitations:**

* Extreme lighting may reduce accuracy
* Similar faces may be confused
* Static images can bypass basic spoof prevention
* Partial or occluded faces may not be recognized

---

# 7. Future Improvements

* Blink/movement detection for spoof prevention
* Smooth predictions using consecutive frames
* GUI via Tkinter or Streamlit
* Deep learning models for higher accuracy
* Automated email/notification for attendance logs


# 8. Appendix 

**Sample Dataset Structure:**

```
dataset/
└── Anshika/
    ├── 1.jpg
    ├── 2.jpg
    └── ...
```

**Sample Attendance CSV:**

```
Name, Timestamp
Anshika Singh, 2026-01-29 09:30:00
```


