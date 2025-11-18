from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.font import Font

def save():
    try:
        nm = t1.get().strip()
        rollnum_text = t2.get().strip()
        m1_text = t3.get().strip()
        m2_text = t4.get().strip()
        m3_text = t5.get().strip()

        # ✅ Validation before converting to int/float
        if not nm or not rollnum_text or not m1_text or not m2_text or not m3_text:
            messagebox.showerror("Error", "Please fill all fields before saving.")
            return

        # ✅ Convert safely
        rollnum = int(rollnum_text)
        m1 = float(m1_text)
        m2 = float(m2_text)
        m3 = float(m3_text)

        tot = float(t6.get())
        avg = float(t7.get())
        rem = str(t8.get())
        username = username_entry.get() if 'username_entry' in globals() else ''
        password = password_entry.get() if 'password_entry' in globals() else ''

        db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
        cursor = db.cursor()

        stmt_check = "SELECT * FROM stud_info WHERE stud_rollnum = %s"
        cursor.execute(stmt_check, (rollnum,))
        existing_record = cursor.fetchone()

        if existing_record:
            messagebox.showwarning("Duplicate Entry", f"Roll number {rollnum} already exists!")
        else:
            stmt = ("INSERT INTO stud_info (stud_nm, stud_rollnum, m1, m2, m3, tot, avg, remark, username, password) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values = (nm, rollnum, m1, m2, m3, tot, avg, rem, username, password)
            cursor.execute(stmt, values)
            db.commit()
            messagebox.showinfo("Insert Box", "Record inserted successfully")
            clear()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")
    finally:
        try:
            db.close()
        except:
            pass


def calculate():
    m1=float(t3.get())
    m2=float(t4.get())
    m3=float(t5.get())
    total=m1+m2+m3
    txt_text.set(total)
    avg=total/3
    txt_text2.set(avg)

    if(avg>80):
        txt_text3.set("Grade A")
    elif(avg>60 and avg<=80):
        txt_text3.set("GRADE B")
    elif(avg>40 and avg<=60):
        txt_text3.set("GRADE C")
    else:
        txt_text3.set("FAIL")
    pass

def search():
    rollnum_text = t9.get().strip()
    if not rollnum_text:
        messagebox.showerror("Error", "Please enter a Roll Number.")
        return
    if not rollnum_text.isdigit():
        messagebox.showerror("Error", "Roll Number must be numeric.")
        return

    rollnum = int(rollnum_text)
    db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
    cursor = db.cursor()
    stmt = f"SELECT * FROM stud_info WHERE stud_rollnum={rollnum}"
    a = cursor.execute(stmt)
    
    if a == 1:
        row = cursor.fetchone()
        t1.delete(0, "end")
        t2.delete(0, "end")
        t3.delete(0, "end")
        t4.delete(0, "end")
        t5.delete(0, "end")
        t6.delete(0, "end")
        t7.delete(0, "end")
        t8.delete(0, "end")
        t1.insert(0, row[0])
        t2.insert(0, row[1])
        t3.insert(0, row[2])
        t4.insert(0, row[3])
        t5.insert(0, row[4])
        t6.insert(0, row[5])
        t7.insert(0, row[6])
        t8.insert(0, row[7])
        messagebox.showinfo("Search Box", "Record found successfully")
    else:
        messagebox.showinfo("Search Box", "Record not found")

    cursor.close()
    db.commit()

    
def delete():
    rollnum_text = t9.get().strip()
    if not rollnum_text:
        messagebox.showerror("Error", "Please enter a Roll Number to delete.")
        return
    if not rollnum_text.isdigit():
        messagebox.showerror("Error", "Roll Number must be numeric.")
        return

    rollnum = int(rollnum_text)
    db = pymysql.connect(host="localhost", user="root", password="", db="stud_db")
    cursor = db.cursor()
    stmt = f"DELETE FROM stud_info WHERE stud_rollnum={rollnum}"
    cursor.execute(stmt)
    db.commit()
    cursor.close()
    messagebox.showinfo("Delete Box", "Record deleted successfully")
    clear()


def clear():
    t1.delete(0, "end")
    t2.delete(0, "end")
    t3.delete(0, "end")
    t4.delete(0, "end")
    t5.delete(0, "end")
    t6.delete(0, "end")
    t7.delete(0, "end")
    t8.delete(0, "end")

def update():
    nm=str(t1.get())
    rollnum=int(t2.get())
    m1=float(t3.get())
    m2=float(t4.get())
    m3=float(t5.get())
    tot=float(t6.get())
    avg=float(t7.get())
    rem=str(t8.get())
    db=pymysql.connect(host="localhost",user="root",password="",db="stud_db")
    cursor=db.cursor()
    stmt=("UPDATE stud_info set stud_nm='"+nm+"',stud_rollnum="+str(rollnum)+",m1="+str(m1)+",m2="+str(m2)+",m3="+str(m3)+",tot="+str(tot)+",avg="+str(avg)+",remark='"+rem+"' where stud_rollnum="+str(rollnum)+"")
    cursor.execute(stmt)
    cursor.close()
    db.commit()
    messagebox.showinfo("Update Box","Record update successfully ")
    pass
def show_frame(frame):
    frame.tkraise()

# Main window
root = Tk()
root.title("Student Form")
root.resizable(0, 0)
root.geometry("1500x800+200+100")
root.configure(bg='#6A0DAD')
canvas = Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)  
frame_width = 1500
frame_height = 800

login_frame = Frame(canvas, bg="#6A0DAD", width=frame_width, height=frame_height,relief="raised", borderwidth=2)
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=frame_width, height=frame_height)

signup_frame = Frame(canvas, bg="#6A0DAD", width=frame_width, height=frame_height,relief="raised", borderwidth=2)
signup_frame.place(relx=0.5, rely=0.5, anchor="center", width=frame_width, height=frame_height)

#-----login page------
log_label = Label(login_frame, text="Login Here", font=("Times New Roman",30,"bold"),bg='#E6E6FA', fg='#34495E',  relief=RIDGE, bd=8)
log_label.pack(pady=10)

name=Label(login_frame ,text="Username:",font=("Roboto",16,"bold"),bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=5)
name.place(x=550,y=180)
n1=Entry(login_frame,width=35,relief="sunken", borderwidth=3)
n1.place(x=700,y=185)

passw=Label(login_frame,text="Password:",font=("Roboto",16,"bold"),bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=5)
passw.place(x=550,y=270)
n2=Entry(login_frame,width=35,relief="sunken", borderwidth=3)
n2.place(x=700,y=275)

get_started_button = Button(login_frame,text="Get started", font=("Roboto", 14, "bold"),bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=4, command=lambda: show_frame(signup_frame), activebackground="#6A0DAD")
get_started_button.place(x=680,y=400)

# Fonts and Variables
title_font = Font(family="Times New Roman", size=30, weight="bold")
bold_font = Font(family="Roboto", size=12,weight="bold")
txt_text = StringVar()
txt_text2 = StringVar()
txt_text3 = StringVar()

# Title
title = Label(signup_frame, text="Student Form", bg='#E6E6FA', fg='#34495E', font=title_font, relief=RIDGE, bd=8)
title.pack(pady=10, padx=10, fill=X)

l1 = Label(signup_frame, text="Name",font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=5)
l1.place(x=120,y=180)
t1=Entry(signup_frame,width=40)
t1.place(x=240,y=185)

l2=Label(signup_frame,text="Roll No",font=bold_font,bg='#E6E6FA',bd=5,fg='#34495E',relief=RAISED)
l2.place(x=800,y=180)
t2=Entry(signup_frame,width=40)
t2.place(x=920,y=185)

l3=Label(signup_frame,text="S1 marks",font=bold_font,bg='#E6E6FA', bd=5,fg='#34495E',relief=RAISED)
l3.place(x=120,y=240)
t3=Entry(signup_frame,width=40)
t3.place(x=240,y=245)

l4=Label(signup_frame,text="S2 marks",font=bold_font,bg='#E6E6FA',bd=5,fg='#34495E',relief=RAISED)
l4.place(x=800,y=240)
t4=Entry(signup_frame,width=40)
t4.place(x=920,y=245)

l5=Label(signup_frame,text="S3 marks",font=bold_font,bg='#E6E6FA',bd=5,fg='#34495E',relief=RAISED)
l5.place(x=120,y=300)
t5=Entry(signup_frame,width=40)
t5.place(x=240,y=305)

l6=Label(signup_frame,text="Total marks",font=bold_font,bg='#E6E6FA',bd=5,fg='#34495E',relief=RAISED)
l6.place(x=120,y=400)
t6=Entry(signup_frame,text="",textvariable=txt_text,width=40,state="readonly")
t6.place(x=240,y=405)

l7=Label(signup_frame,text="Average",font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=5)
l7.place(x=800,y=400)
t7=Entry(signup_frame,text="",textvariable=txt_text2,width=40,state="readonly")
t7.place(x=920,y=405)

l8 = Label(signup_frame, text="Remark ",font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=5)
l8.place(x=120,y=460)
t8=Entry(signup_frame,text="",textvariable=txt_text3,width=40,state="readonly")
t8.place(x=240,y=465)


b1=Button(signup_frame,text="Calculate",width=20,command=calculate,font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=4)
b1.place(x=500,y=330)
b2=Button(signup_frame,text="Save",width=20,command=save,font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=4)
b2.place(x=500,y=490)
b3=Button(signup_frame,text="Delete",width=20,command=delete,font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=4)
b3.place(x=720,y=615)
b4=Button(signup_frame,text="Search",width=20,command=search,font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=4)
b4.place(x=120,y=615)
b5=Button(signup_frame,text="Update",width=20,command=update,font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=4)
b5.place(x=420,y=615)
b6=Button(signup_frame,text="Clear Form",width=20,command=clear,font=bold_font,bg='#E6E6FA',fg='#34495E',relief=RAISED,bd=3)
b6.place(x=1020,y=615)
t9=Entry(signup_frame,width=18)
t9.place(x=170,y=590)

show_frame(login_frame)
root.mainloop()

