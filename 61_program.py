import mysql.connector

conn= mysql.connector.connect(
    host = "localhost",
    user = "root",

    password = ""
)
cursor =conn.cursor()

cursor.execute("create database if not exists dbStudent")
cursor.execute("USE dbStudent")

cursor.execute("""
    create table if not exists Studentinfo(
        student_id INT AUTO_INCREMENT primary key,
        student_name varchar(100),
        stream varchar(30),
        college_name varchar(100),
        contact_number varchar(50),
        remarks int 
    )
""")

print("Table create successfully")

name = input("Enter student name:")
stream = input("Enter stream:")
college = input("Enter college name:")
contact = input("Enter contact:")
remarks = int(input("Enter marks:"))
# insert
sql = "insert into Studentinfo(student_name,stream,college_name,contact_number,remarks) values(%s,%s,%s,%s,%s)"
data = (name,stream,college,contact,remarks)

cursor.execute(sql,data)

conn.commit()
print("record inserted.")
conn.close()

cursor.execute("select * from Studentinfo")
