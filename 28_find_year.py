from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = date.today().year
turn60 = year + (60 - age)

print(name, "will turn 60 in", turn60)