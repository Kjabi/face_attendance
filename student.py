import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x790+0+0")
        self.root.title("face recoginaton system")
#=========================variable=========================
        self.var_NAME=StringVar()
        self.var_CLASS=StringVar()
        self.var_ROLLNO=StringVar()
        self.var_SECTION=StringVar()
        self.var_STUDENTID=StringVar()
        self.var_PHONENO=StringVar()
        self.var_CITY=StringVar()
        self.var_BLOODGROUP=StringVar()
        self.var_FATHERNAME=StringVar()
        
        #back img


        img = Image.open(r"/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/images/neon-01 (1) copy.jpeg")

        img=img.resize((1800,1100))
        self.photoimg=ImageTk.PhotoImage(img)

        f1_ilb=Label(self.root,image=self.photoimg)
        f1_ilb.place(x=0,y=0,width=1800,height=1100)




        #title of the program

        title_lbl=Label(f1_ilb,text="STUDENT MANAGEMENT",font=("times new roman",50,"bold"))
        title_lbl.place(x=330,y=40,width=1000,height=100)

        #frames

        main_frame=Frame(f1_ilb,bd=2)
        main_frame.place(x=20,y=145,width=1640,height=900)

        #=====================left frame=========================
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DEATILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=780,height=850)

        #getting student information coloum

        studentname_lable=Label(left_frame,bd=2,text="NAME OF THE STUDENT",font=("times new roman",20,"bold"))
        studentname_lable.grid(row=0,column=0,padx=0,sticky=W)

        studentname_lable_entry=ttk.Entry(left_frame,textvariable=self.var_NAME,width=30,font=("times new roman",12,"bold"))
        studentname_lable_entry.grid(row=0,column=1,padx=2,sticky=W)

        #classs

        studentclass_lable=Label(left_frame,bd=2,text="CLASS",font=("times new roman",20,"bold"))
        studentclass_lable.grid(row=3,column=0,padx=0,sticky=W)

        search_combo=ttk.Combobox(left_frame,textvariable=self.var_CLASS,font=("times new roman",15,"bold"),state="readonly",width=15)
        search_combo["values"]=("CLASS","1","2","3","4","5","6","7","8","9","10","11","12")
        search_combo.current(0)
        search_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #rollno

        studentrollno_lable=Label(left_frame,bd=2,text="ROLL NUMBER",font=("times new roman",20,"bold"))
        studentrollno_lable.grid(row=6,column=0,padx=0,sticky=W)

        studentrollno_lable_entry=ttk.Entry(left_frame,textvariable=self.var_ROLLNO,width=30,font=("times new roman",15,"bold"))
        studentrollno_lable_entry.grid(row=6,column=1,padx=2,sticky=W)

        #section

        studentsection_lable=Label(left_frame,bd=2,text="SECTION",font=("times new roman",20,"bold"))
        studentsection_lable.grid(row=9,column=0,padx=0,sticky=W)


        BLOOD_combo=ttk.Combobox(left_frame,textvariable=self.var_SECTION,font=("times new roman",12,"bold"),state="readonly",width=15)
        BLOOD_combo["values"]=("SECTION","A","B")
        BLOOD_combo.current(0)
        BLOOD_combo.grid(row=9,column=1,padx=2,pady=10,sticky=W)

        #student id

        studentid_lable=Label(left_frame,bd=2,text="ADDMISION NUMBER",font=("times new roman",20,"bold"))
        studentid_lable.grid(row=12,column=0,padx=0,sticky=W)

        studentid_lable_entry=ttk.Entry(left_frame,textvariable=self.var_STUDENTID,width=30,font=("times new roman",12,"bold"))
        studentid_lable_entry.grid(row=12,column=1,padx=2,sticky=W)

        #phonenumber

        studentphoneno_lable=Label(left_frame,bd=2,text="PHONE NUMBER",font=("times new roman",20,"bold"))
        studentphoneno_lable.grid(row=15,column=0,padx=0,sticky=W)

        studentphoneno_lable_entry=ttk.Entry(left_frame,textvariable=self.var_PHONENO,width=30,font=("times new roman",12,"bold"))
        studentphoneno_lable_entry.grid(row=15,column=1,padx=2,sticky=W)

        #CITY

        studentcity_lable=Label(left_frame,bd=2,text="CITY",font=("times new roman",20,"bold"))
        studentcity_lable.grid(row=18,column=0,padx=0,sticky=W)

        studentcity_lable_entry=ttk.Entry(left_frame,textvariable=self.var_CITY,width=30,font=("times new roman",12,"bold"))
        studentcity_lable_entry.grid(row=18,column=1,padx=2,sticky=W)

        #blood group

        studentblood_lable=Label(left_frame,bd=2,text="BLOOD GROUP",font=("times new roman",20,"bold"))
        studentblood_lable.grid(row=21,column=0,padx=0,sticky=W)

        BLOOD_combo=ttk.Combobox(left_frame,textvariable=self.var_BLOODGROUP,font=("times new roman",15,"bold"),state="readonly",width=15)
        BLOOD_combo["values"]=("BLOOD GROUP","A+","B+","AB+","O+","A-","B-","O-","AB-")
        BLOOD_combo.current(0)
        BLOOD_combo.grid(row=21,column=1,padx=2,pady=10,sticky=W)


       

        #FATHER NAME

        studentfather_lable=Label(left_frame,bd=2,text="FATHER NAME",font=("times new roman",20,"bold"))
        studentfather_lable.grid(row=24,column=0,padx=0,sticky=W)

        studentfather_lable_entry=ttk.Entry(left_frame,textvariable=self.var_FATHERNAME,width=30,font=("times new roman",12,"bold"))
        studentfather_lable_entry.grid(row=24,column=1,padx=2,sticky=W)

        #ratio button
        self.var_RATIOBUTTON1=StringVar()

        ratiobutton_no1=Radiobutton(left_frame,variable=self.var_RATIOBUTTON1,text="TAKE PHOTO SAMPLE",value="Yes")
        ratiobutton_no1.grid(row=27,column=0)

        
        ratiobutton_no2=Radiobutton(left_frame,variable=self.var_RATIOBUTTON1,text="NO PHOTO SAMPLE",value="No")
        ratiobutton_no2.grid(row=27,column=1)

        #save button

        savebutton_1=Button(left_frame,text="SAVE",command=self.add_data,width=50,font=("times new roman",12,"bold"),bg="white",fg="black")
        savebutton_1.grid(row=30,column=0)

        updatebutton_1=Button(left_frame,text="UPDATE",command=self.update_data,width=50,font=("times new roman",12,"bold"),bg="white",fg="black")
        updatebutton_1.grid(row=30,column=1)


        deletebutton_1=Button(left_frame,text="DELETE",command=self.delete_data,width=50,font=("times new roman",12,"bold"),bg="white",fg="black")
        deletebutton_1.grid(row=33,column=0)


        resetbutton_1=Button(left_frame,text="RESET",command=self.reset_data,width=50,font=("times new roman",12,"bold"),bg="white",fg="black")
        resetbutton_1.grid(row=33,column=1) 

        #photo sample button

        photosample_button=Button(left_frame,text="TAKE YOUR PHOTO",command=self.generate_dataset,width=50,font=("times new roman",12,"bold"),bg="white",fg="black")
        photosample_button.grid(row=38,column=0)

        update_photosample=Button(left_frame,text="UPDATE YOUR PHOTO SAMPLE",width=50,font=("times new roman",12,"bold"),bg="white",fg="black")
        update_photosample.grid(row=38,column=1)



        left_frame2=LabelFrame(left_frame,bd=2,relief=RIDGE,text="HOW TO USE ",font=("times new roman",12,"bold"))
        left_frame2.place(x=0,y=420,width=760,height=435)



        read_me=Label(left_frame2,bd=2,text="HOW TO USE:",font=("times new roman",28,"bold"))
        read_me.grid(row=1,column=0,padx=0,sticky=W)

        read_me1=Label(left_frame2,bd=2,text="STEP 1:FILL THE DETAILS CORRECTLY",font=("times new roman",20,"bold"))
        read_me1.grid(row=2,column=0,padx=0,sticky=W)
        read_me2=Label(left_frame2,bd=2,text="STEP 2:TAKE CLEAR PHOTO AND ADD TO YOUR DETAILS",font=("times new roman",20,"bold"))
        read_me2.grid(row=3,column=0,padx=0,sticky=W)
        read_me3=Label(left_frame2,bd=2,text="STEP 3:UPDATE YOUR PHOTO",font=("times new roman",20,"bold"))
        read_me3.grid(row=4,column=0,padx=0,sticky=W)
        read_me4=Label(left_frame2,bd=2,text="STEP 4:CHECK WEATHER YOUR DETAILS ADDED CORRECTLY",font=("times new roman",20,"bold"))
        read_me4.grid(row=5,column=0,padx=0,sticky=W)






        #==============search frame===============
       
        rigtht_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="SEARCH HERE",font=("times new roman",12,"bold"))
        rigtht_frame.place(x=800,y=10,width=820,height=850)


        search_frame=Label(rigtht_frame,text="SEARCH",font=("times new roman",12,"bold"),bg="#CC8899",fg="white")
        search_frame.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        search_combo=ttk.Combobox(rigtht_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("SELECT","ROLLNO","PHONE_NO")
        search_combo.current(0)
        search_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(rigtht_frame,width=30,font=("times new roman",12,"bold"))
        search_entry.grid(row=1,column=2,padx=2,sticky=W)


        search_button=Button(rigtht_frame,text="SEARCH",width=30,font=("times new roman",12,"bold"),bg="white",fg="black")
        search_button.grid(row=1,column=3)

        show_all=Button(rigtht_frame,text="SHOW ALL",width=27,font=("times new roman",12,"bold"),bg="white",fg="black")
        show_all.grid(row=1,column=4)


        #=========================details frame============================

        details_frame=Frame(rigtht_frame,bd=2,bg="white",relief=RIDGE)
        details_frame.place(x=5,y=50,width=800,height=750)


        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(details_frame,columns=("NAME","CLASS","ROLLNUMBER","SECTION","STUDENTID","PHONENO","CITY","BLOODGROUP","FATHERNAME","PHOTOSAMPLE"))


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("NAME",text="NAME")
        self.student_table.heading("CLASS",text="CLASS")
        self.student_table.heading("ROLLNUMBER",text="ROLL NO")
        self.student_table.heading("SECTION",text="SECTION")
        self.student_table.heading("STUDENTID",text="STUDENT ID")
        self.student_table.heading("PHONENO",text="PHONE NO")
        self.student_table.heading("CITY",text="CITY")
        self.student_table.heading("BLOODGROUP",text="BLOOD GROUP")
        self.student_table.heading("FATHERNAME",text="FATHERNAME")
        self.student_table.heading("PHOTOSAMPLE",text="PHOTO SAMPLE")
        self.student_table["show"]="headings"

        self.student_table.column("NAME",width=100)
        self.student_table.column("CLASS",width=100)
        self.student_table.column("ROLLNUMBER",width=100)
        self.student_table.column("SECTION",width=100)
        self.student_table.column("STUDENTID",width=100)
        self.student_table.column("PHONENO",width=100)
        self.student_table.column("CITY",width=100)
        self.student_table.column("BLOODGROUP",width=100)
        self.student_table.column("FATHERNAME",width=100)
        self.student_table.column("PHOTOSAMPLE",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
     #========================function decation=====================

    def add_data(self):
        if (self.var_NAME.get()==""or self.var_ROLLNO.get()=="" or self.var_CITY=="" or self.var_STUDENTID==""):
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abisheek@123",database="face_regonination_project")
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                
                                                                            self.var_NAME.get(),
                                                                            self.var_CLASS.get(),
                                                                            self.var_ROLLNO.get(),
                                                                            self.var_SECTION.get(),
                                                                            self.var_STUDENTID.get(),
                                                                            self.var_PHONENO.get(),
                                                                            self.var_CITY.get(),
                                                                            self.var_BLOODGROUP.get(),
                                                                            self.var_FATHERNAME.get(),
                                                                            self.var_RATIOBUTTON1.get()

                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCESSS!","Student details has been added sucessfully",parent=self.root)
            except Exception as s:
                messagebox.showerror("ERROR!",f"Due To:{str(s)}",parent=self.root)


 #=====================fetch data===============                                                                          
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Abisheek@123",database="face_regonination_project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


   # ===========================get curser=======================
    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content.get("values", [])

        if data and len(data) >= 10:
            self.var_NAME.set(data[0])
            self.var_CLASS.set(data[1])
            self.var_ROLLNO.set(data[2])
            self.var_SECTION.set(data[3])
            self.var_STUDENTID.set(data[4])
            self.var_PHONENO.set(data[5])
            self.var_CITY.set(data[6])
            self.var_BLOODGROUP.set(data[7])
            self.var_FATHERNAME.set(data[8])
            self.var_RATIOBUTTON1.set(data[9])
        else:
            print("DEBUG: No data found or data is incomplete:", data)
            messagebox.showerror("Selection Error", "No data found or incomplete row selected.")


#====================update fucntion===================
    def update_data(self):
        if self.var_NAME.get() == "" or self.var_ROLLNO.get() == "" or self.var_CITY.get() == "":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
        else: 
            try:
                update = messagebox.askyesno("Update", "Do You Want To Update The Student Details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Abisheek@123",
                        database="face_regonination_project"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET
                            name = %s,
                            class = %s,
                            roll_no = %s,
                            section = %s,
                            phone_no = %s,
                            city = %s,
                            blood_group = %s,
                            father_name = %s,
                            gender = %s
                        WHERE student_id = %s
                    """, (
                        self.var_NAME.get(),
                        self.var_CLASS.get(),
                        self.var_ROLLNO.get(),
                        self.var_SECTION.get(),
                        self.var_PHONENO.get(),
                        self.var_CITY.get(),
                        self.var_BLOODGROUP.get(),
                        self.var_FATHERNAME.get(),
                        self.var_RATIOBUTTON1.get(),   # assuming this is gender
                        self.var_STUDENTID.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)

                else:
                    return

            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)


#=====================delete function=================
    def delete_data(self):
        if self.var_STUDENTID.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                print("Student ID to delete:", self.var_STUDENTID.get())  # Debug line

                delete = messagebox.askyesno("REALLY", "DO YOU WANT TO DELETE THIS STUDENT DETAILS", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Abisheek@123",
                        database="face_regonination_project"
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE student_id = %s"
                    val = (self.var_STUDENTID.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Student details have been successfully deleted", parent=self.root)
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to {str(e)}", parent=self.root)



    #=================reset details==============
    def reset_data(self):
        self.var_NAME.set(""),
        self.var_CLASS.set("CLASS"),
        self.var_ROLLNO.set(""),
        self.var_SECTION.set("SECTION"),
        self.var_STUDENTID.set(""),
        self.var_PHONENO.set(""),
        self.var_CITY.set(""),
        self.var_BLOODGROUP.set("BLOOD GROUP"),
        self.var_FATHERNAME.set(""),
        self.var_RATIOBUTTON1.set("")

    #================= generate data or take photo sample=============


    def generate_dataset(self):
        if self.var_NAME.get() == "" or self.var_ROLLNO.get() == "" or self.var_CITY.get() == "":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Abisheek@123",
                database="face_regonination_project"
            )
            my_cursor = conn.cursor()

            # Determine next student ID
            my_cursor.execute("SELECT MAX(student_id) FROM student")
            result = my_cursor.fetchone()
            id = 1 if result[0] is None else int(result[0]) + 1  # <--- fixed here

            # Insert new student record
            my_cursor.execute("""
                INSERT INTO student (student_id, name, class, roll_no, section, phone_no, city, blood_group, father_name, photosample)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                id,
                self.var_NAME.get(),
                self.var_CLASS.get(),
                self.var_ROLLNO.get(),    # var_ROLLNO is fine as a variable, but in DB column it's roll_no
                self.var_SECTION.get(),
                self.var_PHONENO.get(),
                self.var_CITY.get(),
                self.var_BLOODGROUP.get(),
                self.var_FATHERNAME.get(),
                "Yes"
            ))


            conn.commit()
            conn.close()
            self.fetch_data()

            # === Capture facial images using OpenCV ===
            face_classifier = cv2.CascadeClassifier("/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/haarcascade_frontalface_default.xml")

            def face_crop(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                if len(faces) == 0:
                    return None
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]

            cap = cv2.VideoCapture(0)
            img_id = 0
            os.makedirs("data", exist_ok=True)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                face = face_crop(frame)
                if face is not None:
                    img_id += 1
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_path = f"data/user.{id}.{img_id}.jpg"
                    cv2.imwrite(file_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 images
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Dataset Generation Completed!!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

                


                    

                
                           


                    
    
                    


        




if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()