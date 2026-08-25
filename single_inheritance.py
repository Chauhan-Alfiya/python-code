class Person(object):
    def __init__(self,name,id):
        self.name =name
        self.id = id

    def display(self):
        print(self.name,self.id)

class Student(Person):
    def __init__(self,name,id,stud_id):
        Person.__init__(self,name,id)
        self.stud_id = stud_id

    def show(self):
        print(self.stud_id)

emp = Student("alfiya",10,5667)
emp.display()
emp.show()
