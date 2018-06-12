class Human:
    
    def __init__(self):
        print "Human created!"
        self.age = 0
        self.name = "default"

    @property
    def getName(self):
        print self.name
    
    @getName.setter 
    def getName(self,name):
        self.name = name

    @getName.deleter
    def getName(self):
        print "delete now!"
        # self.name = "defaulAgain"

    @property
    def getAge(self):
        print self.age
    


Adam = Human()

Adam.getName = "Adam"

print Adam.getName
del Adam.getName
# print Adam.name
# Adam.getAge

