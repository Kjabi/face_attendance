from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from face_recognition import FaceRecognition
from student import student
from train import Train

import os

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        # Common image path (iCloud)
        IMAGE_PATH = r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/images/fusion-08.jpeg"

        # === Background Image ===
        if os.path.exists(IMAGE_PATH):
            bg_img = Image.open(IMAGE_PATH).resize((1800, 1100))
            self.photoimg = ImageTk.PhotoImage(bg_img)

            bg_label = Label(self.root, image=self.photoimg)
            bg_label.place(x=0, y=0, width=1800, height=1100)
        else:
            print("Image not found at:", IMAGE_PATH)
            return

        # === Title ===
        title_lbl = Label(bg_label, text="FACE ATTENDANCE SYSTEM", font=("times new roman", 50, "bold"), fg="black")
        title_lbl.place(x=330, y=40, width=1000, height=100)

        # === Button Image ===
        img_icon = Image.open(IMAGE_PATH).resize((250, 250))
        self.btn_img = ImageTk.PhotoImage(img_icon)

        # === Row 1 Buttons ===
        self.create_button(bg_label, "STUDENT DETAILS", self.student_details, 150, 200)
        self.create_button(bg_label, "FACE DETECTOR",self.face_attandance, 700, 200)
        self.create_button(bg_label, "ATTENDANCE", None, 1250, 200)

        # === Row 2 Buttons ===
        self.create_button(bg_label, "TRAIN DATA", self.train_data, 150, 700)
        self.create_button(bg_label, "ABOUT US", None, 700, 700)
        self.create_button(bg_label, "ATTENDANCE", None, 1250, 700)

    # === Create button helper ===
    def create_button(self, parent, text, command, x, y):
        img_button = Button(parent, image=self.btn_img, cursor="hand2", command=command if command else None)
        img_button.place(x=x, y=y, width=250, height=250)

        text_button = Button(parent, text=text, cursor="hand2", command=command if command else None,
                             font=("times new roman", 25, "bold"), fg="black")
        text_button.place(x=x, y=y + 252, width=250, height=40)

    # === Button Functions ===
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_attandance(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)


# === Run Program ===
if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    print("Starting Face Recognition App...")
    root.mainloop()

   