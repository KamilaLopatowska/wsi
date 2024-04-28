from tabulate import tabulate

#określenie czasu produkcji elementów
czas_gra = 1 #int(input("Czas produkcji gry (w tygodniach): "))
czas_opakowanie = 1 #int(input("Czas produkcji opakowania (w tygodniach): "))
czas_karty = 1#int(input("Czas produkcji zestawu kart (w tygodniach): "))
czas_karton = 1 #int(input("Czas produkcji kartonu (w tygodniach): "))
czas_plastik = 1 #int(input("Czas produkcji plastikowej części (w tygodniach): "))

#oreślenie startowej dostępności

dostępnosc_gra = 0 #int(input("Początkowa dostępność gry (w sztukach): "))
dostepnosc_opak = 0 #int(input("Początkowa dostępność opakowań (w sztukach): "))
dostepnosc_kart = 0 #int(input("Początkowa dostępność zestawów kart (w sztukach): "))
dostepnosc_karton = 0 #int(input("Początkowa dostępność kartonów (w sztukach): "))
dostepnosc_plastik = 0 #int(input("Początkowa dostępność plastikowych części (w sztukach): "))

#ilość produktów potrzebnych na wskazany dzień
ilosc = int(input("Podaj ilość gier, które potrzebujesz: "))
dzien = input("Podaj ile jest dni na realizację zamówienia: ")

#dostepnosc_gra = int(input("Początkowa dostępność gry (w sztukach): "))
dostepnosc_gra = 10

ilosc_ostateczna = dostepnosc_gra - ilosc
#zależność w ilości między produktami różnych poziomów

ile_opak = 1 #int(input("Ile opakowań potrzebujesz do jednej gry?"))
ile_kart = 20 #int(input("Ile kart potrzebujesz do jednej gry?"))
ile_karton = 4 #int(input("Ile kartonu potrzebujesz do jednego opakowania?"))
ile_plastik = 2 #int(input("Ile plastiku potrzebujesz do jednego opakowania?"))

#database
gra = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne złożenie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""]}
gra[dzien][0] = ilosc
for i in range(1, int(dzien)+1):
    gra[str(i)][1] = dostepnosc_gra
gra[dzien][2] = ilosc - dostepnosc_gra
gra[str(int(dzien)-czas_gra)][3] = ilosc - dostepnosc_gra

opakowanie = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""]}
opakowanie[str(int(dzien)-czas_gra-czas_opakowanie)][3] = (ilosc - dostepnosc_gra)*ile_opak - dostepnosc_opak

karty = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""]}
karty[str(int(dzien)-czas_gra-czas_karty)][3] = (ilosc - dostepnosc_gra)*ile_kart - dostepnosc_kart

karton = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""]}
karton[str(int(dzien)-czas_gra-czas_opakowanie-czas_karton)][3] = ((ilosc - dostepnosc_gra)*ile_opak - dostepnosc_opak)* ile_karton - dostepnosc_karton
plastik = {"dzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "zamówienie", "zaplanowany odbiór"],
        "1": ["","","","",""],
        "2": ["","","","",""],
        "3": ["","","","",""],
        "4": ["","","","",""],
        "5": ["","","","",""],
        "6":["","","","",""],
        "7":["","","","",""]}
plastik[str(int(dzien)-czas_gra-czas_opakowanie-czas_plastik)][3] = ((ilosc - dostepnosc_gra)*ile_opak - dostepnosc_opak)* ile_plastik - dostepnosc_plastik

poziom0 = tabulate(gra, headers = "keys")
poziom1_1 = tabulate(opakowanie, headers = "keys")
poziom1_2 = tabulate(karty, headers = "keys")
poziom2_1 = tabulate(karton, headers = "keys")
poziom2_2 = tabulate(plastik, headers = "keys")

print(f'{poziom0}\n {poziom1_1}\n{poziom1_2}\n{poziom2_1}\n{poziom2_2}')