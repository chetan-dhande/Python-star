class student:
    def getstudent(self):
        self.name=input("name :")
        self.age=int(input("age :"))

class testMarks (student):
    def getMarks(self):
        self.english=int(input("English :"))
        self.Maths=int(input("Maths :"))
        self.physics=int(input("Physics :"))


class result(testMarks):
    def display(self):
        print("Hello",self.name,"You are",self.age,"Years old.")
        print("Your Total marks is ",self.english+self.Maths+self.physics)


re=result()
re.getstudent()
re.getMarks()
re.display()