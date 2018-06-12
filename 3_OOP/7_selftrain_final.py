#class, enum, class variable/method, subClass, property, getter/setter, magic function/repr/deleter/add

class Gender:
    Male=1
    Female=2


class Human(object):

    Power = 0

    def __init__(self,first,last,age,gender):
        print "Human Created!"
        self.First = first
        self.Last = last
        self.Age = age
        self.Gender = gender
        # self.Name = self.First + self.Last
    
    def getHumanInfo(self):
        print "first:{}, last:{}, age:{}, gender{}, power:{}".format(self.First,self.Last,self.Age,self.Gender,self.Power)

    @classmethod
    def changeAllPower(cls,val):
        cls.Power = val

    @property
    def Name(self):
        return self.First + self.Last
    
    def __repr__(self):
        return "This is Human Class."

    def __add__(self,other):
        print "__add__"
        return self.Age + other.Age

    @Name.deleter
    def Name(self):
        self.First = ""

class NewHuman(Human):
    def __init__(self,first,last,age,gender,speed):
        super(NewHuman,self).__init__(first,last,age,gender)
        self.Speed = speed

    def getHumanInfo(self):
        print "first:{}, last:{}, age:{}, gender{}, power:{}, speed:{}".format(self.First,self.Last,self.Age,self.Gender,self.Power,self.Speed)

Human.changeAllPower(10)

Adam = Human("Adam","Yang",2,Gender.Male)
Adam.getHumanInfo()

Adam.Last = "Chen"

del Adam.Name
print Adam.Name

Eva = Human("Eva","Chen",3,Gender.Female)
print Adam + Eva

# Eva = Human("Eva","Chen",0,Gender.Female)
# Eva.Power = 2
# Eva.getHumanInfo()

# Dante = NewHuman("Dante","Wong",1,Gender.Male,33.1)
# Dante.getHumanInfo()