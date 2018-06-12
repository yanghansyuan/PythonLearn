

class Artwork:

    excuter = "myself"
    productiontime =0
    budge =0

    def __init__(self, excuter, spendTime, money):
        # self.excuter = excuter #comment out with default excuter.
        self.productiontime = spendTime
        self.budge = money
        print "Artwork is born. "

    def ideaCreate(self, myKeyword="not thing"):
        print "Idea is created. It's about " + myKeyword + "." 

    def whoIsArtist(self):
        print "excuter is " + self.excuter + "."



newArtwork = Artwork("John",10,1000)
# newArtwork.ideaCreate("stree sign")
newArtwork.ideaCreate()
newArtwork.whoIsArtist()

paperArtwrok = Artwork("livi",10,1000)
paperArtwrok.ideaCreate("use paper to shape.")
paperArtwrok.whoIsArtist()