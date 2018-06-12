

class Employee(object): 

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + " " + last + "@company.com" #onlt set when init once!

    @property #Allow us access class method like acces a variable. like a getter
    def email(self): 
        return "{}.{}@email.com".format(self.first,self.last)

    @property
    def fullname(self): 
        return "{}{}".format(self.first,self.last)
    
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name!")
        self.first = None
        self.last = None

emp_1 = Employee("Corey","Schafer",50000 )

emp_1.fullname = "micheal johnson"

# del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

