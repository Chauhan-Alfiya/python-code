import mysql.connector
import tkinter as tk
from tkinter import ttk,messagebox

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = conn.cursor()

cursor.execute("create database if not exists dbStudent")
cursor.execute("use dbStudent")

cursor.execute(
    """
    create table if not exists Studentinfo(
    student_id int auto_increment primary key,
    student_name varchar(100),
    stream varchar(100),
    college_name varchar(100),
    contact_number varchar(15),
    remarks int
    )
"""
)

def insert_student():
    name = name_entry.get()
    stream = stream_entry.get()
    college = college_entry.get()
    contact = contact_entry.get()
    try:
        remarks = int(remarks_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid marks")
        return


    if not name or not stream or not college or not contact or not remarks_entry.get():
        messagebox.showerror("please fill all fileds.")
        return
    
    sql = "insert into Studentinfo(student_name,stream,college_name,contact_number,remarks) values(%s,%s,%s,%s,%s)"
    data = (name,stream,college,contact,remarks)

    cursor.execute(sql,data)
    conn.commit()

    messagebox.showinfo("Success","record inserted successfully.")

    show_student()

def show_student():

    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("select * from Studentinfo")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


# GUI

root = tk.Tk()
root.title("Student ManageMent")
root.geometry("850x500")

title = tk.Label(
    root,
    text ="Student Information",
    font = ("Arial",20,"bold")
)
title.pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)


tk.Label(
    form_frame,
    text=" Student Name:",
    font = ("Arial",12)
).grid(row=0,column=0,padx=10,pady=5)

name_entry=tk.Entry(
    form_frame,
    width=35,
    font=("Arial",12)
)
name_entry.grid(row=0,column=1,padx=10,pady=5)


tk.Label(
    form_frame,
    text=" Stream:",
    font = ("Arial",12)
).grid(row=1,column=0,padx=10,pady=5)

stream_entry=tk.Entry(
    form_frame,
    width=35,
    font=("Arial",12)
)
stream_entry.grid(row=1,column=1,padx=10,pady=5)

tk.Label(
    form_frame,
    text=" College Name:",
    font = ("Arial",12)
).grid(row=2,column=0,padx=10,pady=5)

college_entry=tk.Entry(
    form_frame,
    width=35,
    font=("Arial",12)
)
college_entry.grid(row=2,column=1,padx=10,pady=5)

tk.Label(
    form_frame,
    text=" Contact:",
    font = ("Arial",12)
).grid(row=3,column=0,padx=10,pady=5)

contact_entry=tk.Entry(
    form_frame,
    width=35,
    font=("Arial",12)
)
contact_entry.grid(row=3,column=1,padx=10,pady=5)

tk.Label(
    form_frame,
    text = "Rrmarks:",
    font=("Arial",12)
).grid(row=4,column=0,padx=10,pady=5)
remarks_entry=tk.Entry(
    form_frame,
    width=35,
    font=("Arial",12)
)
remarks_entry.grid(row=4,column=1,padx=10,pady=5)

insert_button =tk.Button(
    form_frame,
    text = "Insert",
    command=insert_student,
    bg= "blue",
    fg="white",
    width=20
)
insert_button.grid(row=5,column=0,columnspan=2,pady=10)


table_frame = tk.Frame(root)
table_frame.pack(fill="both",padx=10,pady=10,expand=True)

columns=(
    "ID",
    "Name",
    "Stream",
    "College",
    "Contact",
    "Marks"
)
tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    tree.heading(column,text=column)
    tree.column(column,width=120)

tree.pack(fill="both",expand=True)

show_student()

def close_app():
    cursor.close()
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()

