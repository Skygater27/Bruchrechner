from tkinter import * 
from tkinter import messagebox
from bruch_rechner import *

class bruch_GUI:
    
    def __init__(self):

        self.rechner=Bruch_rechner()

        fenster=Tk()
        fenster.geometry("700x400")
        fenster.title("Bruch-Rechner")

# Bruch 1
        self.la1string=StringVar()
        self.la1string.set("Bruch 1")
        self.la1=Label(fenster,width=8, textvariable=self.la1string).grid(row=1, column=1, columnspan= 2)

        self.en1string=StringVar()
        self.en1string.set("1")
        self.en1=Entry(fenster,width=8, textvariable=self.en1string).grid(row=2, column=1, columnspan= 2)

        self.en2string=StringVar()
        self.en2string.set("1")
        self.en2=Entry(fenster,width=8, textvariable=self.en2string).grid(row=3, column=1, columnspan= 2)

# x Zeichen-

        self.la4string=StringVar()
        self.la4string.set("+")
        self.la4=Label(fenster,width=8, textvariable=self.la4string).grid(row=2, column=3, columnspan= 2)

# Bruch 2
        self.la2string=StringVar()
        self.la2string.set("Bruch 2")
        self.la2=Label(fenster,width=8, textvariable=self.la2string).grid(row=1, column=5, columnspan= 2)

        self.en3string=StringVar()
        self.en3string.set("1")
        self.en3=Entry(fenster,width=8, textvariable=self.en3string).grid(row=2, column=5, columnspan= 2)

        self.en4string=StringVar()
        self.en4string.set("1")
        self.en4=Entry(fenster,width=8, textvariable=self.en4string).grid(row=3, column=5, columnspan= 2)

# = Zeichen

        self.la5string=StringVar()
        self.la5string.set("=")
        self.la5=Label(fenster,width=8, textvariable=self.la5string).grid(row=2, column=7, columnspan= 2)
        
# Ergebnis
        self.la3string=StringVar()
        self.la3string.set("Ergebnis")
        self.la3=Label(fenster,width=8, textvariable=self.la3string).grid(row=1, column=9, columnspan= 2)

        self.la5string=StringVar()
        self.la5string.set("1")
        self.la5=Label(fenster,width=8, textvariable=self.la5string).grid(row=2, column=9, columnspan= 2)

        self.la6string=StringVar()
        self.la6string.set("1")
        self.la6=Label(fenster,width=8, textvariable=self.la6string).grid(row=3, column=9, columnspan= 2)

# Label fÃ¼r abstand
        self.la7string=StringVar()
        self.la7string.set("")
        self.la7=Label(fenster,width=8, textvariable=self.la7string).grid(row=4, column=1, columnspan= 8)

# Button +
        self.bu1string=StringVar()
        self.bu1string.set("+")
        self.bu1=Button(fenster,width=8, textvariable=self.bu1string, command=self.mult_zeichen).grid(row=5, column=1, columnspan= 2)

# Button -
        self.bu2string=StringVar()
        self.bu2string.set("-")
        self.bu2=Button(fenster,width=8, textvariable=self.bu2string,command=self.mult_zeichen).grid(row=5, column=3, columnspan= 2)

# Button *
        self.bu3string=StringVar()
        self.bu3string.set("*")
        self.bu3=Button(fenster,width=8, textvariable=self.bu3string,command=self.mult_zeichen).grid(row=5, column=5, columnspan= 2)

# Button /
        self.bu4string=StringVar()
        self.bu4string.set("/")
        self.bu4=Button(fenster,width=8, textvariable=self.bu4string,command=self.mult_zeichen).grid(row=5, column=7, columnspan= 2)

# def funktionen
    def rechenzeichen_bruch(self):
        if self.rechner.rechenart == "add":
            self.la4string.set("+")

        elif self.rechner.rechenart == "sub":
            self.la4string.set("-")

        elif self.rechner.rechenart == "div":
            self.la4string.set("/")

        elif self.rechner.rechenart == "mul":
            self.la4string.set("*")

        else:
            print("Feher bei rechenzeichen_Bruch()")

    # def rechnen(self):
    #     if self.rechner.rechenart == "add":
    #         self.rechner.addieren(self.en1string, self.en2string, self.en3string, self.en4string)

    #     elif self.rechner.rechenart == "sub":
    #         self.rechner.subtrahieren(self.en1string, self.en2string, self.en3string, self.en4string)

    #     elif self.rechner.rechenart == "div":
    #         self.rechner.dividieren(self.en1string, self.en2string, self.en3string, self.en4string)

    #     elif self.rechner.rechenart == "mul":
    #         self.rechner.multiplizieren(self.en1string, self.en2string, self.en3string, self.en4string)

    #     else:
    #         print("Feher bei rechnen()")

    def mult_zeichen(self):
        self.rechner.multipizieren(self.en1string, self.en2string, self.en3string, self.en4string)
        self.rechenzeichen_bruch()

    def datenAktualisieren(self):
        pass
        
    def anzeigeAktualisieren(self):
        pass


# Main loop
if __name__ == '__main__':
    dasFenster = bruch_GUI()
    mainloop()