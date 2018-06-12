class wingChung:

    nowForm = "none"
    name = ""
    master =""
    power = 100

    def __init__(self, name, form, master):
        self.name = name
        self.nowForm = form
        self.master = master
        
        # print "name: " + self.name + ", " + "start form is " + self.nowForm + ". And learn from Sifu"  + self.master + "." #original one, bad
        # print("name: {}, start form is: {}. And learn from Sifu: {}.".format(self.name,self.nowForm,self.master))
        print("name: {0}, start form is: {1}. And learn from Sifu: {2}.".format(self.name,self.nowForm,self.master))

    def learnNewForm(self,form):
        nowForm  = form
        print "learn form:" + nowForm + "."

    def switchUseForm(self,form):
        self.nowForm = form
        print "switch form: " + self.nowForm + "."

    def getNowForm(self):
        print "now use form :" + self.nowForm + "."

    def getNowPower(self):
        print("The power of {} is: {}.".format(self.name,self.power))

    def resetAllPower(self, power):
        wingChung.power = power #set class variable for all.
        print("reset all, now class variable is :{}".format(wingChung.power))
    
    def setPower(self,power):
        self.power = power

myWingChung = wingChung("yhs","aaa","Chen Sifu")
myWingChung2 = wingChung("livi", "aaa","yhs")

myWingChung.setPower(150)
myWingChung2.setPower(180)

myWingChung.getNowPower()
myWingChung2.getNowPower()

myWingChung.resetAllPower(200) # reset all with class variable
myWingChung.getNowPower() #not effect because already set individually 
myWingChung2.getNowPower() #not effect because already set individually 
myWingChung3 = wingChung("user", "aaa","yhs")
myWingChung3.getNowPower() #default val has been reset from class variable 

print(myWingChung.__dict__)
print(myWingChung2.__dict__)
print(myWingChung3.__dict__)

# myWingChung.learnNewForm("bbb")
# myWingChung.getNowForm()
# myWingChung.switchUseForm("bbb")
# myWingChung.getNowForm()
# myWingChung2.getNowForm()

