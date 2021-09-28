#this code is written in python3 and is owned by Santino Pircher

#Q: Speichern Sie Ihren Namen in einer Variable. Worauf sollten Sie bei der Benennung von Variablen achten?
#A: Man sollte bei der bennenung der Variablen darauf achten, dass diese nicht mit Zahlen beginnen und sprechende Namen haben. 

myName = "Santino Pircher"
myAge = 21

#Geben Sie folgenden Text auf der Konsole aus: „Name ist Alter Jahre alt“. Lesen Sie die Werte Name und Alter aus den entsprechenden Variablen aus, die Sie bereits angelegt haben.
print(f"{myName} ist {myAge} Jahre alt")

#Q: Entscheiden Sie für die folgenden Bezeichner, ob sie gültige Variablennamen in Python sind: 1a, size, circle_radius, test-variable, testVariable, 
#   correct?, attention!, for, xqwoi.

#A: 1a : NEIN, size : JA, circle_radius : JA, test-variable : NEIN, testVariable : JA, correct? : NEIN, attention! : NEIN, for : NEIN, xqwoi : JA

#Wo liegt der Unterschied zwischen den Variablen a, b und c? Welche Typen haben sie? Überlegen sie sich zuerst Ihre Antwort, und überprüfen Sie sie dann mittels type().

a = 42    # Integer
b = ’42 ’ # String
c = 42.0  # Float

#Speichern Sie den Radius eines Kreises in einer Variablen. Berechnen Sie Umfang und Flächeninhalt dieses Kreises und geben Sie beides auf der Konsole aus.

radius = 5
pi = 3.14159265359
#Wiedergabe des Radius in der Konsole:
print(2*radius*pi)
#Wiedergabe des Flächeninhalts in der Konsole:
print(radius*radius*pi)
