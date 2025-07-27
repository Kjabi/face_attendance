from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import numpy as np
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System - Train Faces")

        # Load background image (update path as needed)
        img = Image.open(r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/images/fusion-08.jpeg")
        img = img.resize((1800, 1100))
        self.photoimg = ImageTk.PhotoImage(img)

        f1_lbl = Label(self.root, image=self.photoimg)
        f1_lbl.place(x=0, y=0, width=1800, height=1100)

        title_lbl = Label(f1_lbl, text="TRAIN FACES", font=("times new roman", 50, "bold"), fg="black")
        title_lbl.place(x=330, y=40, width=1000, height=100)

        b1 = Button(f1_lbl, text="TRAIN DATASET", command=self.train_classifier, cursor="hand2", font=("times new roman", 25, "bold"), fg="black")
        b1.place(x=0, y=600, width=1700, height=80)

    def train_classifier(self):
        data_dir = r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/data"

        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory does not exist:\n{data_dir}")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            try:
                # Skip non-image files
                if not image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                    print(f"Skipped non-image file: {image_path}")
                    continue

                # Open image in grayscale
                img = Image.open(image_path).convert('L')
                image_np = np.array(img, 'uint8')

                # Filename format expected: user.<id>.<img_num>.jpg
                filename = os.path.basename(image_path)
                id = int(filename.split('.')[1])

                faces.append(image_np)
                ids.append(id)

                cv2.imshow("Training", image_np)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Error processing file {image_path}: {e}")

        ids = np.array(ids)

        # Check if face module exists
        if not hasattr(cv2, 'face'):
            messagebox.showerror("Error", "cv2.face module not found. Please install opencv-contrib-python.")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed successfully!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
