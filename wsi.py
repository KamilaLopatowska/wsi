import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tabulate'])

from tabulate import tabulate

#Ilość produktów potrzebnych na wskazany dzień
ilosc = int(input("Podaj ilość gier, które potrzebujesz: "))
dzien = input("Podaj ile jest dni na realizację zamówienia (1-10): ")

while ilosc <= 0:
    ilosc = int(input("Podaj POPRAWNĄ (dodatnią) ilość gier, które potrzebujesz: "))

#Safety stock
question = input(" Czy chcesz określić minimalny poziom produktów na stanie? Naciśnij enter, żeby potwierdzić, jeśli nie wpisz 1 i enter")
if question == "":
    min_gra = int(input("Jaka powinna być minimalna liczba gier w magazynie?"))
    min_opak = int(input("Jaka powinna być minimalna liczba opakowań w magazynie?"))
    min_kart = int(input("Jaka powinna być minimalna liczba kart w magazynie?"))
    min_karton = int(input("Jaka powinna być minimalna liczba kartonów w magazynie?"))
    min_plastik = int(input("Jaka powinna być minimalna liczba plastików w magazynie?"))
else:
    min_gra = 0
    min_opak = 0
    min_kart = 0
    min_karton = 0
    min_plastik = 0

#Określenie startowej dostępności
dostepnosc_gra = int(input("Początkowa dostępność gry (w sztukach): "))
if dostepnosc_gra < min_gra:
    print("Liczba w magazyniue nie może być poniżej minimalnego poziomu produktów na stanie")
    dostepnosc_gra = int(input("Początkowa dostępność gry (w sztukach): "))

if dostepnosc_gra >= ilosc:
    in_stock = True
else:
    in_stock = False
    dostepnosc_opak = int(input("Początkowa dostępność opakowań (w sztukach): "))
    if dostepnosc_opak < min_opak:
        print("Liczba w magazyniue nie może być poniżej minimalnego poziomu produktów na stanie")
        dostepnosc_opak = int(input("Początkowa dostępność gry (w sztukach): "))

    dostepnosc_kart = int(input("Początkowa dostępność kart (w sztukach): "))
    if dostepnosc_kart < min_kart:
        print("Liczba w magazyniue nie może być poniżej minimalnego poziomu produktów na stanie")
        dostepnosc_kart = int(input("Początkowa dostępność gry (w sztukach): "))

    dostepnosc_karton = int(input("Początkowa dostępność kartonów (w sztukach): "))
    if dostepnosc_karton < min_kart:
        print("Liczba w magazyniue nie może być poniżej minimalnego poziomu produktów na stanie")
        dostepnosc_karton = int(input("Początkowa dostępność gry (w sztukach): "))
    
    dostepnosc_plastik = int(input("Początkowa dostępność plastikowych części (w sztukach): "))
    if dostepnosc_plastik < min_karton:
        print("Liczba w magazyniue nie może być poniżej minimalnego poziomu produktów na stanie")
        dostepnosc_plastik = int(input("Początkowa dostępność gry (w sztukach): "))

#Określenie czasu produkcji poszczególnych elementów
if dostepnosc_gra >= ilosc:
    in_stock = True
else:
    in_stock = False
    czas_gra = int(input("Czas produkcji gry (w dniach): "))
    czas_opakowanie = int(input("Czas produkcji opakowania (w dniach): "))
    czas_karty = int(input("Czas produkcji karty (w dniach): "))
    czas_karton = int(input("Czas produkcji kartonu (w dniach): "))
    czas_plastik = int(input("Czas produkcji plastikowej części (w dniach): "))

#Zależność między ilościami produktów różnych poziomów
if dostepnosc_gra >= ilosc:
    in_stock = True
else:
    in_stock = False
    ile_opak = int(input("Ile opakowań potrzebujesz do jednej gry?"))
    ile_kart = int(input("Ile kart potrzebujesz do jednej gry?"))
    ile_karton = int(input("Ile kartonu potrzebujesz do jednego opakowania?"))
    ile_plastik = int(input("Ile plastiku potrzebujesz do jednego opakowania?"))

#Sprawdzenie zapotrzebowania netto na produkty
gra_netto = ilosc - dostepnosc_gra + min_gra 

if in_stock == False:
    
    opak_netto = gra_netto*ile_opak - dostepnosc_opak + min_opak
    if opak_netto <= 0:
        opak_netto = 0

    karty_netto = gra_netto*ile_kart - dostepnosc_kart + min_kart
    if karty_netto <= 0:
        karty_netto = 0

    plastik_netto = opak_netto*ile_plastik - dostepnosc_plastik + min_plastik
    if plastik_netto <= 0:
        plastik_netto = 0
    
    karton_netto = opak_netto*ile_karton - dostepnosc_karton + min_karton
    if karton_netto <= 0:
        karton_netto = 0

# Słowniki
gra = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne złożenie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""],
        "8": ["","","","",""],
        "9": ["","","","",""],
        "10": ["","","","",""]}

opakowanie = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""],
        "8": ["","","","",""],
        "9": ["","","","",""],
        "10": ["","","","",""]}

karty = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""],
        "8": ["","","","",""],
        "9": ["","","","",""],
        "10": ["","","","",""]}

karton = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""],
        "8": ["","","","",""],
        "9": ["","","","",""],
        "10": ["","","","",""]}

plastik = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""],
        "8": ["","","","",""],
        "9": ["","","","",""],
        "10": ["","","","",""]}

#Tabele i ich wypełnienie
if in_stock == False:

    try:
    #databases

        #poziom 0
        gra[dzien][0] = ilosc

        for i in range(1, int(dzien)+1):
            gra[str(i)][1] = dostepnosc_gra
        for i in range(int(dzien)+1,11):
            gra[str(i)][1] = min_gra
        
        gra[dzien][2] = gra_netto + min_gra

        gra[str(int(dzien)-czas_gra)][3] = gra_netto

        gra[dzien][4] = gra_netto


        #poziom 1 - opakowanie
        opakowanie[str(int(dzien)-czas_gra)][0] = gra_netto*ile_opak

        for i in range(1, int(dzien)-czas_gra+1):
            opakowanie[str(i)][1] = dostepnosc_opak
        for i in range(int(dzien)-czas_gra+1,11):
            opakowanie[str(i)][1] = min_opak

        opakowanie[str(int(dzien)-czas_gra)][2] = opak_netto

        opakowanie[str(int(dzien)-czas_gra - czas_opakowanie)][3] = opak_netto

        opakowanie[str(int(dzien)-czas_gra)][4] = opak_netto


        #poziom 1 - karty
        karty[str(int(dzien)-czas_gra)][0] = ile_kart*gra_netto

        for i in range(1, int(dzien)-czas_gra+1):
            karty[str(i)][1] = dostepnosc_kart
        for i in range(int(dzien)-czas_gra+1,11):
            karty[str(i)][1] = min_kart

        karty[str(int(dzien)-czas_gra)][2] = karty_netto

        karty[str(int(dzien)-czas_gra - czas_karty)][3] = karty_netto

        karty[str(int(dzien)-czas_gra)][4] = karty_netto


        #poziom 2 - karton
        if (opak_netto)*ile_karton <= 0:
            karton[str(int(dzien)-czas_gra-czas_opakowanie)][0] = 0
        else:
            karton[str(int(dzien)-czas_gra-czas_opakowanie)][0] = (opak_netto)*ile_karton

        for i in range(1, int(dzien)-czas_opakowanie-czas_gra+1):
            karton[str(i)][1] = dostepnosc_karton
        for i in range(int(dzien)-czas_opakowanie-czas_gra+1,11):
            karton[str(i)][1] = min_karton

        karton[str(int(dzien)-czas_gra-czas_opakowanie)][2] = karton_netto

        karton[str(int(dzien)-czas_gra-czas_opakowanie-czas_karton)][3] = karton_netto

        karton[str(int(dzien)-czas_gra-czas_opakowanie)][4] = karton_netto
    
    
        #poziom 2 - plastik
        if (opak_netto)*ile_plastik <= 0:
            plastik[str(int(dzien)-czas_opakowanie-czas_gra)][0] = 0
        else:
            plastik[str(int(dzien)-czas_opakowanie-czas_gra)][0] = (opak_netto)*ile_plastik

        for i in range(1, int(dzien)-czas_opakowanie-czas_gra+1):
            plastik[str(i)][1] = dostepnosc_plastik
        for i in range(int(dzien)-czas_opakowanie-czas_gra+1,11):
            plastik[str(i)][1] = min_plastik

        plastik[str(int(dzien)-czas_opakowanie-czas_gra)][2] = plastik_netto

        plastik[str(int(dzien)-czas_opakowanie-czas_gra-czas_plastik)][3] = plastik_netto

        plastik[str(int(dzien)-czas_opakowanie-czas_gra)][4] = plastik_netto
        

        # tabele
        poziom0 = tabulate(gra, headers = "keys", tablefmt="grid")
        poziom1_1 = tabulate(opakowanie, headers = "keys", tablefmt="grid")
        poziom1_2 = tabulate(karty, headers = "keys", tablefmt="grid")
        poziom2_1 = tabulate(karton, headers = "keys", tablefmt="grid")
        poziom2_2 = tabulate(plastik, headers = "keys", tablefmt="grid")



        #wyświetlanie wyniku
        print(f'Poziom 0 - gra\nsafe stock: {min_gra}\n{poziom0}\n\nPoziom 1 - opakowanie\nsafe stock: {min_opak}\n{poziom1_1}\n\nPoziom 1 - karty\nsafe stock: {min_kart}\n{poziom1_2}\n\nPoziom 2 - karton\nsafe stock: {min_karton}\n{poziom2_1}\n\nPoziom 2 - plastik\nsafe stock: {min_plastik}\n{poziom2_2}')
    except KeyError:
        print("Nie da się wykonać zamówienia w podanym czasie")
else:
    print("Zamówienie możliwe do wysłania/odebrania od zaraz")