#class variable, static method, subClass, magic function, property, getter/setter, enum

class Gender:
    Male =1
    Female =2

class MoveMode:
    walk = 1
    fly = 2


class Human(object): #inherit from object for new class style

    Movement = MoveMode.walk 

    def __init__(self, name, age, gender):
        print "Human Create!"
        self.Name = name
        self.Age = age
        self.Gender = gender
        # self.Power = 1 * self.Age

    def gethumanInfo(self):
        return "Human info, Name: {}, Age: {}".format(self.Name, self.Age)
    

    def move(self):
        return self.Movement

    @classmethod
    def evolution (cls,newMode):
        cls.Movement = newMode

    @property #Getter: use this property function to replace original property calculation with out changing interface for instance
    def Power(self):
        print "property here"
        return 1 * self.Age
    
    @Power.setter
    def Power(self, val):
        print "Setter here"
        self._Power = 0.003 # need "_" here inpython 2.7!

    def __repr__(self):
        return "It's a human"

class NewHuman(Human):
    def __init__(self,name,age,gender,newMoode):
        super(NewHuman,self).__init__(name,age,gender)


Human.evolution(MoveMode.fly) #change all class method

# Adam = Human("Adam",1, Gender.Male)
# print Adam.name()
# print Adam.move()

# Eva = Human("Eva",1,Gender.Female)
# print Eva.name()
# Eva.Movement = MoveMode.walk #only change one class
# print Eva.move()

# Dante = NewHuman("Dante",5,Gender.Male, MoveMode.fly )
# print Dante.Name
# print Dante.gethumanInfo()
# Dante.Age = 10 #should change power by here
# print Dante.gethumanInfo()
# print Dante.Power

Adam = Human("Adam",1, Gender.Male)
Adam.Power = 100
print Adam.Power
print (Adam.__repr__())
print Adam.Name.__str__()
