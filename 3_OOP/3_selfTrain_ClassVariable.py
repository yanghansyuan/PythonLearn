

class Human :
    protected = False
    age = 0
    height = 0
    gender = "none"
    intellegence = 140

    def __init__(self, age, height, gender):
        self.age = age
        self.height = height
        self.gender = gender
    def increaseIntellegence(self, num):
        self.intellegence = self.intellegence + num




Adam = Human(20,180,"male")
Shawa = Human(19,160,"female")
Human.protected = True
Shawa.protected = False

Adam.increaseIntellegence(20)

# print(Adam.__dict__)
# print(Shawa.__dict__)
print(Adam.protected)
print(Shawa.protected)

print(Adam.intellegence)
print(Shawa.intellegence)