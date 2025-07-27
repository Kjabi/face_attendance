# Face Recognition Attendance System

This project is a **Python-based face recognition attendance system** with a user-friendly GUI and MySQL integration for storing student data and attendance logs. It's ideal for use in schools, colleges, or small organizations to automate attendance tracking.

## 🔧 Tech Stack

- **Frontend GUI**: Tkinter (Python)
- **Face Recognition**: OpenCV with Haar Cascade + LBPHFaceRecognizer
- **Backend Database**: MySQL
- **Language**: Python 3.x

## 📁 Features

- Add and manage student information.
- Capture face dataset via webcam.
- Train face recognition model.
- Recognize faces in real-time and mark attendance.
- Attendance logs saved in `.csv` and/or MySQL database.

## 📷 Face Image Format

Captured images are saved as:

data/user.<student_id>.<image_number>.jpg

shell
Copy
Edit

## 🗂️ Folder Structure

face_attendance/
│
├── data/ # Captured face images
├── attendance/ # Attendance CSV logs
├── trainer/ # Trained model file (classifier.xml)
├── student.py # Student info GUI and DB entry
├── train.py # Model training logic
├── face_recognition.py # Real-time recognition and attendance
├── database.py # MySQL connectivity
├── main.py # Main entry point
└── requirements.txt # Required Python packages

bash
Copy
Edit

## 🛠️ Setup Instructions

### 1. Clone the Repo

bash
git clone https://github.com/Kjabi/face_attendance.git
cd face_attendance
2. Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt



4. MySQL Setup
Create a database named face_regonination_project and a table student with the following schema:

CREATE TABLE student (
  student_id VARCHAR(20) PRIMARY KEY,
  name VARCHAR(100),
  class VARCHAR(50),
  roll_no VARCHAR(20),
  section VARCHAR(10),
  phone_no VARCHAR(15),
  city VARCHAR(100),
  blood_group VARCHAR(10),
  father_name VARCHAR(100),
  gender VARCHAR(10),
  photosample VARCHAR(20)
);

✅ TODO
 Student registration with photo sample

 Face dataset creation

 Model training

 Real-time face recognition

 Attendance logging

 Email alert integration (future)

 Admin dashboard (future)
 🧠 How to Use
📥 Step 1: Add Student Details
bash
Copy
Edit
python student.py
Fill in all fields (name, roll no, class, etc.)

Click on Take Photo Sample to collect 70 images of the student’s face

Click Save Student

This stores the info in MySQL and saves face images to data/.

🧪 Step 2: Train the Face Model
bash
Copy
Edit
python train.py
This will train the LBPH face recognizer using the images in data/ folder.

The trained model is saved as trainer/classifier.xml.

📸 Step 3: Recognize Faces and Mark Attendance
bash
Copy
Edit
python face_recognition.py
It opens the webcam and starts recognizing trained faces.

When a known face is detected, it logs attendance to a .csv file inside attendance/.

🚀 Optional: Launch from Main Menu
bash
Copy
Edit
python main.py
(If main.py integrates all modules together)

📝 Sample Attendance Log
pgsql
Copy
Edit
attendance/attendance_27-07-2025.csv

| Student ID | Name       | Date       | Time     |
|------------|------------|------------|----------|
| 1234       | John Smith | 27-07-2025 | 09:10 AM |
✅ Features Completed
 Student data entry GUI

 Webcam face capture

 Model training

 Real-time recognition

 Attendance logging (CSV)

📌 Author
K.j. Abisheek
B.Tech Artificial Intelligence and Data Science
GitHub

⭐️ Give a Star
If you like this project, consider giving it a ⭐ on GitHub!

