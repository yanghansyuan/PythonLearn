from enum import Enum

class Gender(Enum):
    Male = 1
    Female =2


class BodyType(Enum):
    Fit = 1
    Slim = 2
    Heavy = 3


class Human:
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
    
    @classmethod
    def changeStartEye(cls,eye):
        cls.Eyes = eye

    @classmethod
    def from_str(clas,human_str):
        age, gender, bodytype = human_str.split("-")
        
        Human(age,gender,bodytype)

    @staticmethod
    def growUp(speed):
        pass

Adam = Human(0, Gender.Male, BodyType.Heavy)
Eve = Human(0, Gender.Female, BodyType.Slim)

human_str  = "3-Gender.Male-BodyType.Fit"

dante = Human.from_str(human_str)

Human.changeStartEye(1)
Eve.Eyes = 3

print(Adam.Eyes)
print(Eve.Eyes)