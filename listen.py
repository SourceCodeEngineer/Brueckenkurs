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

#WILL BE CONTINUED!
