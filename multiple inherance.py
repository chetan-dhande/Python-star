class Person:
    def __init__(self,personname,personage):
        self.name=personname
        self.age=personage

    def showName (self):
        print(self.name)

    def showage(self):
        print(self.age)

class student:
    def __init__(self,studentid):
        self.studentid=studentid

    def getid (self):
        print(self.studentid)

class resident (Person,student):
    def __init__(self,name,age,id):
        Person.name=name
        Person.age=age
        student.studentid=id

r=resident('john',30,20)
r.showName()
r.showage()
r.getid()


y=Person('amit',10)
y.showname()
y.showage()
#y.getid()