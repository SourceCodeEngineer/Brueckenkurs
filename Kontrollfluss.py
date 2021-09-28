#this code is written in python3 and is owned by Santino Pircher

#Geben Sie die Zahlen von 25 bis 1 rückwärts aus (25, 24, . . . , 1).

zahl = 25         #Variable "zahl" erstellt mit dem Anfangswert 25

while zahl > 0:     #While-Schleife bis die Zahl Größer 0 ist da wir 0 nicht ausgeben möchten
    print(zahl)     #Ausgabe der Zahl in der Komandozeile
    zahl -= 1       #Die Zahl um 1 verringern
  
#Geben Sie alle Zahlen von 1 bis inklusive 100 aus, die entweder durch 3 oder durch 7 teilbar sind.

zahl = 1            #Variable erstellt

while zahl <= 100:  #solange Variable kleiner oder gleich 100 ist wird die schleife ausgeführt
    if zahl % 3 == 0 or zahl % 7 == 0:  #wenn die Zahl durch 3 mit 0 Rest dividiert werden kann ODER durch 7 mit 0 Rest dividiert werden kann, wird die zahl ausgegeben
        print(zahl)
        zahl += 1      #Zahl um 1 erhöht
    else:
        zahl += 1      #Zahl um 1 erhöht
        
#Geben Sie alle Zahlen von 1 bis inklusive 100 aus, die durch 8, aber nicht durch 24, teilbar sind.
zahl = 1

while zahl <= 100:
    if zahl % 8 == 0 and not zahl % 24 == 0:    #Hier das selbe wie oben nur mit dem KEYWORD NOT!
        print(zahl)
        zahl += 1
    else:
        zahl += 1
        
# Geben Sie die ersten n Fibonacci-Zahlen aus. Es gilt Fn = Fn−1 + Fn−2, F1 = 1 und F0 = 0. Die
#Variable n wird vorher beliebig gesetzt (Beispiel: n = 42).   

nterms = 100

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print(n1)
else:
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
#Geben Sie alle Vielfachen der Zahlen 2 bis inklusive 10 aus, die kleiner als 100 sind. Beginnen
#Sie mit den Vielfachen von 2: 2, 4, . . . , 98. Dann kommen alle Vielfachen von 3 (3, 6, . . . , 99),
#und so weiter.

zahl = 2
counter = 0

while zahl <= 10:
    while counter <= 100:
        if counter % zahl == 0:
            print(counter)
            counter += 1
        else:
            counter += 1
    counter = 0
    zahl += 1
