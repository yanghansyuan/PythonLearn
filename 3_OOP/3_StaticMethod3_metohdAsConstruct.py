

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
    

emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)


emp_str_1 = "Jone-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_1 = "Jane-Doe-90000"


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
