#this code is written in python3 and is owned by Santino Pircher

#Schreiben Sie eine Funktion sub(list_a, list_b), die list_b von list_a „subtrahiert“. Mit
#anderen Worten: Es sollen all jene Elemente von list_a zurückgegeben werden, die nicht in
#list_b enthalten sind.

def sub(list_a, list_b):
    new_list = []
    for element in list_a:
        if element in list_b:
            continue
        else:
            new_list.append(element)

    return new_list
    
#Bestimmen Sie das Minimum einer Liste numerischer Werte (Integer und Float).

def min(list):
    counter = list[0]
    for element in list:
        if element < counter:
            counter = element

    return counter
    
#Füllen Sie eine Liste der Länge 20 mit Zufallszahlen. Überlegen Sie sich einen einfachen Algorithmus, 
#mit dem eine Liste nur mit Vergleich- und Vertauschoperationen sortiert werden kann. Wie
#könnte ein solcher Algorithmus aussehen? Versuchen Sie zuerst einen Algorithmus zu entwickeln,
#bevor Sie etwas implementieren! Sie sollten insbesondere in der Lage sein, einem Bekannten zu
#erklären, wie dieser Algorithmus funktioniert!
import random

list = []

while len(list) <= 20:
    list.append(random.randint(1,10000))

def sortList(array):
    length = len(array)

    for item in range(length):
        minimum = item

        for i in range(item + 1, length):
            if array[i] < array[minimum]:
                minimum = i

        (array[item], array[minimum]) = (array[minimum], array[item])
        
sortList(list)

#Implementieren Sie eine Funktion add(point_a, point_b), die zwei Punkte eines karthesischen
#Koordinatensystems addiert. Es gilt [a, b] + [x, y] = [a + x, b + y].

def add(point_a, point_b):
    new_list = []
    new_list.append(point_a[0] + point_b[0])
    new_list.append(point_a[1] + point_b[1])
    return new_list


#Schreiben Sie eine Funktion dist(point_a, point_b), die die Distanz zwischen zwei Punkten
#in einem karthesischen Koordinatensystems zurückgibt.

def dist(point_a, point_b):
    return ((point_b[0]-point_a[0])*(point_b[0]-point_a[0]))+((point_b[1]-point_a[1])*(point_b[1]-point_a[1]))


#Implementieren Sie eine binäre Uhr, die die aktuelle Uhrzeit ausgibt (siehe auch https://de.
#wikipedia.org/wiki/Bin%C3%A4re_Uhr). Suchen Sie zuerst einen passenden Befehl, der Ihnen
#die aktuelle Systemzeit zurückgibt. Wandeln Sie dann sowohl Stunde (0–23) als auch Minute
#(0–59) in eine Binärzahl um. Üblicherweise verwendet man binäre LEDs, die leuchten oder eben
#nicht. Bilden Sie dieses Verhalten nach, indem Sie ein X für leuchtend, und ein O für nicht-
#leuchtend auf der Kommandozeile ausgeben. Beispiel:

from datetime import datetime

now = datetime.now()

current_hour = int(now.strftime("%H"))
current_minute = int(now.strftime("%M"))

binary_hour = list(format(current_hour, "b"))
binary_minute = list(format(current_minute, "b"))

xo_hour = []
xo_minute = []

for element in binary_hour:
    if element == "0":
        xo_hour.append("O")
    elif element == "1":
        xo_hour.append("X")

for element in binary_minute:
    if element == "0":
        xo_minute.append("O")
    elif element == "1":
        xo_hour.append("X")

print("".join(xo_hour))
print("".join(xo_minute))
