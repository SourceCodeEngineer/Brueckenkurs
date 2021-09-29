#this code is written in python3 and is owned by Santino Pircher

#Schreiben Sie ein Programm, mit dem zufällige Passwörter generiert werden können. Welche Zeichenklassen 
#(Großbuchstaben, Ziffern, Sonderzeichen, . . . ) zugelassen sind, sollte konfigurierbar
#sein. Implementieren Sie auch eine Funktion, mit der Sie beliebig viele Passwörter beliebiger
#Länge generieren können.

import string
import random

print("------------Passwort Generator------------")

select_gross = int(input("Wollen Sie Großbuchstaben zulassen? Wenn Ja, drücken Sie 1 wenn Nein drücken Sie 2: "))
select_klein = int(input("Wollen Sie Kleinbuchstaben zulassen? Wenn Ja, drücken Sie 1 wenn Nein drücken Sie 2: "))
select_zahl = int(input("Wollen Sie Zahlen zulassen? Wenn Ja, drücken Sie 1 wenn Nein drücken Sie 2: "))
select_sonder = int(input("Wollen Sie Sonderzeichen zulassen? Wenn Ja, drücken Sie 1 wenn Nein drücken Sie 2: "))

def choice_by_user(a, b, c, d):
    characters = []
    if a == 1:
        for element in string.ascii_uppercase:
            characters.append(element)
    if b == 1:
        for element in string.ascii_lowercase:
            characters.append(element)
    if c == 1:
        for element in string.digits:
            characters.append(element)
    if d == 1:
        list_sonder = list("!@#$%^&*()")
        for element in list_sonder:
            characters.append(element)

    return characters


def generate_password(characters):
    length = int(input("Enter password length: "))
    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

print(generate_password(choice_by_user(select_gross,select_klein,select_zahl,select_sonder)))
