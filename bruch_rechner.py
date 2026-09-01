from bruch_GUI import *

class Bruch_rechner():



    def __init__(self):

        self.rechenart = "+"

    def addieren(self, zaeler1, nenner1, zaeler2, nenner2):
        print("addieren")
        self.rechenart = "add"
#        return self.rechenart

    def subtrahieren(self, zaeler1, nenner1, zaeler2, nenner2):
        print("subtrahieren")
        self.rechenart = "sub"
#        return self.rechenart


    def dividieren(self, zaeler1, nenner1, zaeler2, nenner2):
        print("dividieren")
        self.rechenart = "div"
#        return self.rechenart

    def multipizieren(self, zaehler1, nenner1, zaehler2, nenner2):
        print("multiplizieren")
        self.rechenart = "mul"
        ergebnis_zaehler= zaehler1 * zaehler2
        ergebnis_nenner = nenner1 * nenner2


#        return self.rechenart
