#class, enum, class variable/method, subClass, property, getter/setter, magic function/repr/deleter/add

class Gender:
    Male =1
    Female =2

class Human(object):

    Defense = 0

    def __init__(self, first, last, age, gender, power):
        print "Human Created!"
        self.First = first
        self.Last =  last
        self.Age = age
        self.Gender = gender
        self.Power = power
        # self.Name = self.First + self.Last

    def getHumanInfo(self):
        return "first:{}, last:{}, age:{}, gender:{}, power:{}, defense:{}".format(self.First,self.Last,self.Age,self.Gender,self.Power,self.Defense)
    
    @property
    def Name(self):
        return self.First + self.Last

    @Name.deleter
    def Name(self):
        self.First = ""

    @classmethod
    def changeDefense(cls,val):
        cls.Defense = val
    
    def __repr__(self):
        return "This is a Human!"

    def __add__(self,other):
        return self.Age + other.Age

    

class NewHuman(Human):
    def __init__(self, first, last, age, gender, power,speed):
        super(NewHuman,self).__init__(first, last, age, gender, power)
        self.Speed = speed
        print "New Human Created!"

    def getHumanInfo(self):
        return "first:{}, last:{}, age:{}, gender:{}, power:{}, defense:{}, speed:{}".format(self.First,self.Last,self.Age,self.Gender,self.Power,self.Defense, self.Speed)

Human.changeDefense(10)

Adam = Human("Adam","Chen",1,Gender.Male,1)
# Eva = Human("Eva","Wong",3,Gender.Female,2)

del Adam.Name
print Adam.Name

# print Adam + Eva



# Eva = Human("Eva","Wong",0,Gender.Female,2)
# Eva.Defense = 2 
# print Eva.getHumanInfo()

# Dante = NewHuman("Dante","Yang",0,Gender.Male,2,0.23)
# print Dante.getHumanInfo()