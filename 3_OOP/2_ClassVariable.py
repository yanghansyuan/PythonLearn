

class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + " " + last + "@company.com"
        Employee.num_of_emps += 1
    
    def fullname(self): #self = instance
        return "{}{}".format(self.first,self.last)

    def applyRaise(self):
        self.pay = int(self.pay * Employee.raise_amount)


    
    

emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)

print("Employee.raise_amount = {}".format(Employee.raise_amount))
emp_1.raise_amount = 1.06
Employee.raise_amount = 1.05 #set class variable for all

print(emp_1.__dict__)
print(emp_2.__dict__)

print("Employee.raise_amount = {}".format(Employee.raise_amount))
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)

