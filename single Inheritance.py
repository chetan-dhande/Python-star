class person:
    def getName (self,name):
        self.name=name
        return self.name
    def isEmployee(self):
        return False

class Employee(person):
    def isEmployee(self):
        return True

emp=person()
print(emp.getName("Ajay"),emp.isEmployee())

emp=Employee()
print(emp.getName("Pallavi"),emp.isEmployee())

