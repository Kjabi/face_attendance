from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import cv2
import os

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        # Load background image
        try:
            img = Image.open(r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/images/fusion-08.jpeg")
            img = img.resize((1800, 1100))
            self.photoimg = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Failed to load image: {e}")
            self.photoimg = None

        if self.photoimg:
            bg_label = Label(self.root, image=self.photoimg)
            bg_label.place(x=0, y=0, width=1800, height=1100)
        else:
            bg_label = Label(self.root, bg="grey")
            bg_label.place(x=0, y=0, width=1800, height=1100)

        # Title Label
        title_lbl = Label(bg_label, text="FACE RECOGNITION", font=("times new roman", 50, "bold"), fg="black")
        title_lbl.place(x=330, y=40, width=1000, height=100)

        # Start Button
        start_btn = Button(
            bg_label, text="START FACE RECOGNITION", cursor="hand2", command=self.face_recog,
            font=("times new roman", 25, "bold"), fg="black"
        )
        start_btn.place(x=0, y=600, width=1700, height=80)

    def mark_attendance(self, student_id, name, student_class, roll_no):
        filename = "/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/schoolattendance.csv"
        header = "student_id,name,class,roll_no,time,date,status\n"

        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%H:%M:%S")

        try:
            if not os.path.exists(filename) or os.path.getsize(filename) == 0:
                with open(filename, "w") as f:
                    f.write(header)

            with open(filename, "r") as f:
                lines = f.readlines()

            already_marked = False
            for line in lines[1:]:
                entry = line.strip().split(",")
                if len(entry) < 7:
                    continue
                if entry[0] == str(student_id) and entry[5] == date_str:
                    already_marked = True
                    break

            if not already_marked:
                with open(filename, "a") as f:
                    f.write(f"{student_id},{name},{student_class},{roll_no},{time_str},{date_str},present\n")
                print(f"[INFO] Attendance marked for {name}")
            else:
                print(f"[INFO] Attendance already marked for {name} today")

        except Exception as e:
            print(f"[ERROR] mark_attendance: {e}")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            conn = None
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="Abisheek@123", database="face_regonination_project"
                    )
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT name FROM student WHERE student_id = %s", (id,))
                    name = my_cursor.fetchone()
                    name = "+".join(name) if name else "Unknown"

                    my_cursor.execute("SELECT class FROM student WHERE student_id = %s", (id,))
                    student_class = my_cursor.fetchone()
                    student_class = "+".join(student_class) if student_class else "Unknown"

                    my_cursor.execute("SELECT roll_no FROM student WHERE student_id = %s", (id,))
                    roll_no = my_cursor.fetchone()
                    roll_no = "+".join(roll_no) if roll_no else "Unknown"

                    student_id = str(id)

                    if confidence > 77:
                        cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Class: {student_class}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll No: {roll_no}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(student_id, name, student_class, roll_no)
                    else:
                        cv2.putText(img, "UNKNOWN FACE", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
                except mysql.connector.Error as e:
                    print(f"[ERROR] MySQL: {e}")
                finally:
                    if conn and conn.is_connected():
                        conn.close()

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/haarcascade_frontalface_default.xml"
        )

        if faceCascade.empty():
            messagebox.showerror("Error", "Failed to load Haarcascade XML file.")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/classifier.xml")

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            messagebox.showerror("Error", "Webcam not detected.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("[ERROR] Failed to grab frame.")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("FACE RECOGNITION", img)

            if cv2.waitKey(1) & 0xFF == ord('z'):
                print("[INFO] Exiting recognition...")
                break

        video_cap.release()
        cv2.destroyAllWindows()

# MAIN
if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
