import mysql.connector

conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
)

cursor = conn.cursor()

cursor.execute(
    "CREATE DATABASE IF NOT EXISTS studentdb" 
)

print("database create")

cursor.execute("USE studentdb")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stud(

    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    mobile INT(100),
    email VARCHAR(100)
    )
    """
)
print("table create successfully.")


insert_query="INSERT INTO stud(firstname,lastname,mobile,email) VALUES(%s,%s,%s,%s)"
val = ("Alfiya","chauhan",68798098,"alfiya@gmail.com")
cursor.execute(insert_query,val)

conn.commit()
print("record inserted")

cursor.execute(" SELECT * FROM stud ")

rows = cursor.fetchall()

for row in rows:
    print(row)


update_query = """

UPDATE stud
SET lastname = "%s" 
WHERE id=%s 
"""
val = ("CHAUHAN",1)
cursor.execute(update_query,val)
conn.commit()
print("data update.")
conn.commit()
cursor.execute(" SELECT * FROM stud ")

rows = cursor.fetchall()

for row in rows:
    print(row)

