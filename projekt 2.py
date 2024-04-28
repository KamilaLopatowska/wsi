from tabulate import tabulate

#ilość produktów potrzebnych na wskazany dzień
ilosc = int(input("Podaj ilość gier, które potrzebujesz: "))
dzien = input("Podaj ile jest tygodni na realizację zamówienia: ")

#dostepnosc_gra = int(input("Początkowa dostępność gry (w sztukach): "))
dostepnosc_gra = 10

ilosc_ostateczna = dostepnosc_gra - ilosc
#zależność w ilości między produktami różnych poziomów

#database
gra = {"tydzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne zmontowanie", "zaplanowany odbiór"],
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

opakowanie = {"tydzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne zmontowanie", "zaplanowany odbiór"],
        "1": ["","2","","",""],
        "2": ["","2","","",""],
        "3": ["","2","","",""],
        "4": ["","2","","18",""],
        "5": ["20","2","18","","18"],
        "6":["","","","40",""],
        "7":["40","","40","","40"]}
karty = {"tydzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne zmontowanie", "zaplanowany odbiór"],
        "1": ["","2","","",""],
        "2": ["","2","","",""],
        "3": ["","2","","",""],
        "4": ["","2","","18",""],
        "5": ["20","2","18","","18"],
        "6":["","","","40",""],
        "7":["40","","40","","40"]}
karton = {"tydzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne zmontowanie", "zaplanowany odbiór"],
        "1": ["","2","","",""],
        "2": ["","2","","",""],
        "3": ["","2","","",""],
        "4": ["","2","","18",""],
        "5": ["20","2","18","","18"],
        "6":["","","","40",""],
        "7":["40","","40","","40"]}
plastik = {"tydzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne zmontowanie", "zaplanowany odbiór"],
        "1": ["","2","","",""],
        "2": ["","2","","",""],
        "3": ["","2","","",""],
        "4": ["","2","","18",""],
        "5": ["20","2","18","","18"],
        "6":["","","","40",""],
        "7":["40","","40","","40"]}
df = tabulate(gra, headers = "keys")
print(df)