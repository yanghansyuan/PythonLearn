

class Employee(object): #inherit for object as "new -style classes"

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + " " + last + "@company.com"
    
    def fullname(self): #self = instance
        return "{}{}".format(self.first,self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 2
    def __init__(self, first, last, pay, pro_lang  ):
        super(Developer,self).__init__(first,last,pay) #witt new-style class, super need to contain class and self as parameter
        self.pro_lang = pro_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super(Manager,self).__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->{}".format(emp.fullname()))

emp_1 = Developer("Corey","Schafer",50000 ,"Python")
emp_2 = Developer("Test","User",60000 ,"Java")

mrg_1 = Manager("sue","smith",90000,[emp_1])
mrg_1.add_emp(emp_2)

mrg_1.print_emps()

print(isinstance(mrg_1,Manager))
print(issubclass(Manager,Employee))
