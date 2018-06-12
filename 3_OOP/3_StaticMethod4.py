

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

    @classmethod
    def from_string(cls, emp_str): #"from" is convention
        first, last, pay = emp_str.split("-")        
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day): #static method don't need access instance or class
        if day.weekday() == 5 or  day.weekday() == 6:
            return False 
        return True

emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)


import datetime
my_date = datetime.date(2018,5,27)

print(Employee.is_workday(my_date))
