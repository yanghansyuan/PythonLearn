

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

    @classmethod
    def set_raise_amt(cls, amount): #cls = class, take class as first variable
        cls.raise_amount = amount
    
    

emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)
emp_1.raise_amount = 0.3 #already set so class variable won't change it.

Employee.set_raise_amt(1.05) #change class's variable for all

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
