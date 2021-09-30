#this code is written in python3 and is owned by Santino Pircher

#Schreiben Sie eine Funktion incr(x), die x + 1 zurückgibt.
def incr(x):
    return x + 1

#Schreiben Sie eine Funktion cmp(a, b), die zwei gegebene Zahlen a und b miteinander vergleicht.
#Ist a < b, gibt die Funktion −1 zurück. Ist a > b, gibt die Funktion 1 zurück. Sind beide Zahlen
#gleich groß, gibt die Funktion 0 zurück.

def cmp(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0
    
#Implementieren Sie eine Funktion leapYear(year), die berechnet, ob es sich beim gegebenen
#Jahr um ein Schaltjahr handelt. Geben Sie entsprechend True oder False zurück. Tipp: Ein
#Schaltjahr ist restlos durch 4 teilbar; jedoch ist ein volles Jahrhundert nur dann ein Schaltjahr,
#wenn es auch durch 400 teilbar ist. Beispiel: 1900 ist kein Schaltjahr, 2000 aber schon.
#Würden Sie in einem Projekt auf eine existierende Lösung zurückgreifen (Library), oder die
#Funktion wie in dieser Übung implementieren?

year = 2000

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
            return True
       else:
           return False
   else:
       return True
else:
   return False

#Programmieren Sie das folgende kleine Spiel: Der Computer „denkt“ sich eine geheime Zahl
#aus. Der Benutzer muss versuchen, diese Zahl in mehreren Versuchen zu erraten. Nach jedem
#Versuch gibt das Spiel aus, ob der Benutzer zu nieder, zu hoch, oder richtig geraten hat. Die
#maximale Anzahl der Versuche und der Wertebereich der Zufallszahlen können vom Benutzer
#gewählt werden. Das Spiel ist beendet, wenn die maximale Anzahl an Versuchen erreicht wurde,
#oder aber der Spieler die geheime Zahl errät. Tipp: Sie können mit userInput = int(input())
#eine Zahl von der Kommandozeile einlesen. Verwenden Sie das Modul random, um Zufallszahlen
#zu erzeugen (http://docs.python.org/3/library/random.html).

import random
obergrenze = int(input("Bitte die Obergrenze eingeben: "))
random_number = random.randrange(1,obergrenze)
versuche = int(input("Bitte die maximalen Versuche eingeben: "))

user_input = 0
counter = 0

while counter < versuche:
    while user_input != random_number:
        user_input = int(input("Bitte rate die Zuffalszahl: "))
        if user_input > random_number:
            print("Du hast zu hoch geraten! Versuch es erneut!")
            counter += 1
        elif user_input < random_number:
            print("Du hast zu niedrig geraten! Versuch es erneut!")
            counter += 1
        else:
            print(f"HURRA! Du hast {counter} Versuche gebraucht um die Zahl zu erraten!")
            
print(f"Schade, die Zahl war {random_number}")
