from tabulate import tabulate


#ilość produktów potrzebnych na wskazany dzień
ilosc = int(input("Podaj ilość gier, które potrzebujesz: "))
dzien = input("Podaj ile jest dni na realizację zamówienia: ")

#zależność w ilości między produktami różnych poziomów

#database
gra = {"tydzień": ["potrzeby brutto", "wstępny zapas", "potrzeby netto", "wstępne zmontowanie", "zaplanowany odbiór"],
        "1": ["","2","","",""],
        "2": ["","2","","",""],
        "3": ["","2","","",""],
        "4": ["","2","","18",""],
        "5": ["20","2","18","","18"],
        "6":["","","","40",""],
        "7":["40","","40","","40"]}
gra[dzien][0] = ilosc
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
