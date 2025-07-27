# Face Recognition Attendance System

A real-time face recognition attendance system using Python, OpenCV, Tkinter, and MySQL. This project allows automatic marking of attendance by recognizing student faces and storing the details securely in a MySQL database.

## 💡 Features

- Student face dataset generation
- LBPH face recognition model training
- Real-time face detection and recognition
- Attendance marking with timestamp
- GUI with Tkinter for user input
- Data storage in MySQL and CSV

## 🛠️ Tech Stack

- Python
- OpenCV
- Tkinter
- MySQL

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kjabi/face_attendance.git
   cd face_attendance


## 🔧 How to Use

Follow these steps to use the Face Recognition Attendance System:

### 1. Generate Dataset
- Open the GUI (`python main.py`).
- Fill in the student details (Name, Roll No, Class, etc.).
- Click the **"Take Photo Sample"** button.
- The system will capture multiple facial images and store them in the `data/` directory.

### 2. Train Model
- After capturing face data, click the **"Train Data"** button.
- This will train the LBPH Face Recognizer using the images and save the model as `classifier.xml`.

### 3. Recognize and Mark Attendance
- Click the **"Face Recognition"** button.
- The webcam will open and start recognizing faces in real-time.
- Once recognized, attendance will be marked automatically and saved in a CSV file.

### 4. View Attendance
- You can view the saved attendance by clicking the **"Attendance"** button in the GUI.

---

📌 **Note:**
- Make sure your MySQL server is running.
- Ensure the `student` table is created in the `face_regonination_project` database before using the system.

