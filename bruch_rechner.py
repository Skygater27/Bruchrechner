from bruch_GUI import *

class Bruch_rechner():



    def __init__(self):

        self.rechenart = "+"
        self.ergebnis_zaehler = 1
        self.ergebnis_nenner = 1

# Kleinster Gemeinsamer Nenner herausfinden
    def k_g_nenner(self, zaehler1, nenner1, zaehler2, nenner2):

        self.kgN = nenner1

        while self.kgN % nenner2 != 0:
            self.kgN += nenner1

        self.faktor1 = self.kgN // nenner1
        self.faktor2 = self.kgN // nenner2

        zaehler1 *= self.faktor1
        zaehler2 *= self.faktor2

        return zaehler1, zaehler2, self.kgN

    def addieren(self, zaehler1, nenner1, zaehler2, nenner2):
        print("addieren")
        self.rechenart = "add"
        zaehler1, zaehler2, self.kgN = self.k_g_nenner(zaehler1, nenner1, zaehler2, nenner2)
        self.ergebnis_zaehler = zaehler1 + zaehler2
        self.ergebnis_nenner = self.kgN


    def subtrahieren(self, zaehler1, nenner1, zaehler2, nenner2):
        print("subtrahieren")
        self.rechenart = "sub"
        zaehler1, zaehler2, self.kgN = self.k_g_nenner(zaehler1, nenner1, zaehler2, nenner2)
        self.ergebnis_zaehler = zaehler1 - zaehler2
        self.ergebnis_nenner = self.kgN



    def dividieren(self, zaehler1, nenner1, zaehler2, nenner2):
        print("dividieren")
        self.rechenart = "div"
        self.ergebnis_zaehler = (zaehler1 * nenner2)
        self.ergebnis_nenner  = (nenner1 * zaehler2)


    def multipizieren(self, zaehler1, nenner1, zaehler2, nenner2):
        print("multiplizieren")
        self.rechenart = "mul"
        self.ergebnis_zaehler = (zaehler1 * zaehler2)
        self.ergebnis_nenner  = (nenner1 * nenner2)
