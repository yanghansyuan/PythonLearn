from enum import Enum

class Gender(Enum):
    Male = 1
    Female =2


class BodyType(Enum):
    Fit = 1
    Slim = 2
    Heavy = 3


class Human(object):
    Age = 0
    Gender = Gender.Male
    BodyShape = BodyType.Fit
    Eyes = 2

    def __init__(self, age, gender, bodyShape ):
        print("hello world, one human created.")
        self.Age = age
        self.Gender = gender
        self.BodyShape = bodyShape
        print("New human info: age:{}, gender:{}, body:{}".format(self.Age, self.Gender, self.BodyShape))
        print("----")


class SuperHuman(Human):
    # power = 100 #no need to define this. why?
    def __init__(self, age, gender, bodyShape, power ):
        super(SuperHuman,self).__init__(age,gender,bodyShape)
        self.power = power

    def addPower(self, power):
        self.power = self.power + power    


Adam = Human(0, Gender.Male, BodyType.Heavy)
Eve = Human(0, Gender.Female, BodyType.Slim)

human_str  = "3-Gender.Male-BodyType.Fit"

dante = SuperHuman(0, Gender.Male, BodyType.Heavy, 100)

dante.addPower(20)
print(dante.power)
