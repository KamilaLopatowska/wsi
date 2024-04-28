class Materiał:
    def __init__(self, nazwa, stan_początkowy, czas_produkcji):
        self.nazwa = nazwa
        self.stan_początkowy = stan_początkowy
        self.czas_produkcji = czas_produkcji
        self.wymagania = []  # Lista wymagań dla danego materiału

    def dodaj_wymaganie(self, materiał, ilość):
        self.wymagania.append((materiał, ilość))

    def oblicz_zapotrzebowanie_netto(self, zapotrzebowanie_tygodniowe):
        # Obliczanie zapotrzebowania netto na dany materiał na podstawie zapotrzebowania na produkty końcowe
        zapotrzebowanie_netto = 0
        for materiał, ilość in self.wymagania:
            zapotrzebowanie_netto += materiał.oblicz_zapotrzebowanie_netto(zapotrzebowanie_tygodniowe) * ilość
        return max(0, zapotrzebowanie_netto - self.stan_początkowy)

    def oblicz_plan_produkcji(self, zapotrzebowanie_tygodniowe):
        # Obliczanie planu produkcji dla danego materiału na podstawie zapotrzebowania netto i czasu produkcji
        zapotrzebowanie_netto = self.oblicz_zapotrzebowanie_netto(zapotrzebowanie_tygodniowe)
        return max(0, zapotrzebowanie_netto / self.czas_produkcji)

def generuj_zapotrzebowanie_tygodniowe(materiał, zapotrzebowanie_tygodniowe):
    # Generowanie zapotrzebowania tygodniowego dla danego materiału
    zapotrzebowanie_tygodniowe = [zapotrzebowanie_tygodniowe] * 7  # Zakładamy takie samo zapotrzebowanie przez cały tydzień
    return zapotrzebowanie_tygodniowe

def generuj_tabelę_mrp(materiały, zapotrzebowanie_tygodniowe):
    # Generowanie tabeli MRP dla wszystkich materiałów na podstawie zapotrzebowania tygodniowego
    nagłówek_tabeli = ["Materiał"] + [f"Dzień {i}" for i in range(1, 8)]
    tabela_mrp = [nagłówek_tabeli]

    for materiał in materiały:
        wiersz = [materiał.nazwa]
        for dzień in range(7):
            zapotrzebowanie_netto = zapotrzebowanie_tygodniowe[dzień]
            plan_produkcji = materiał.oblicz_plan_produkcji(zapotrzebowanie_netto)
            wiersz.append(f"{int(zapotrzebowanie_netto)} / {int(plan_produkcji)}")
        tabela_mrp.append(wiersz)

    return tabela_mrp

def main():
    # Definiowanie materiałów i produktów końcowych w strukturze BOM
    komponent_a = Materiał("Komponent A", stan_początkowy=10, czas_produkcji=1)
    komponent_b = Materiał("Komponent B", stan_początkowy=5, czas_produkcji=2)
    komponent_c = Materiał("Komponent C", stan_początkowy=0, czas_produkcji=1)

    produkt_x = Materiał("Produkt X", stan_początkowy=0, czas_produkcji=3)
    produkt_y = Materiał("Produkt Y", stan_początkowy=0, czas_produkcji=4)

    # Definiowanie zależności ilościowych (struktura BOM)
    produkt_x.dodaj_wymaganie(komponent_a, 2)
    produkt_x.dodaj_wymaganie(komponent_b, 1)

    produkt_y.dodaj_wymaganie(komponent_b, 3)
    produkt_y.dodaj_wymaganie(komponent_c, 2)

    # Generowanie zapotrzebowania tygodniowego dla produktów końcowych
    zapotrzebowanie_tygodniowe_x = generuj_zapotrzebowanie_tygodniowe(produkt_x, 100)  # Zapotrzebowanie na Produkt X
    zapotrzebowanie_tygodniowe_y = generuj_zapotrzebowanie_tygodniowe(produkt_y, 150)  # Zapotrzebowanie na Produkt Y

    # Generowanie tabeli MRP
    tabela_mrp = generuj_tabelę_mrp([produkt_x, produkt_y], zapotrzebowanie_tygodniowe_x)

    # Wyświetlanie tabeli MRP
    for wiersz in tabela_mrp:
        print("\t".join(wiersz))

if __name__ == "__main__":
    main()
