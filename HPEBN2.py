from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=10000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=15000, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                print("A szoba már foglalt ezen a napon.")
                return
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append({'szobaszam': szobaszam, 'datum': datum})
                print(f"A(z) {szobaszam} számú szoba sikeresen foglalva {datum} napra.")
                return
        print("Nincs ilyen szoba.")

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                print(f"A(z) {szobaszam} számú szoba foglalása {datum} napra sikeresen törölve.")
                return
        print("Nincs ilyen foglalás.")

    def foglalasok_listazasa(self):
        print("Foglalások listája:")
        for foglalas in self.foglalasok:
            print(f"Szoba száma: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}")

def main():
    szalloda = Szalloda("Hotel Szép Kilátás")

    egyagyas1 = EgyagyasSzoba(szobaszam=101)
    ketagyas1 = KetagyasSzoba(szobaszam=201)
    ketagyas2 = KetagyasSzoba(szobaszam=202)

    szalloda.uj_szoba(egyagyas1)
    szalloda.uj_szoba(ketagyas1)
    szalloda.uj_szoba(ketagyas2)

    szalloda.foglalas(szobaszam=101, datum="2024-05-24")
    szalloda.foglalas(szobaszam=201, datum="2024-05-25")
    szalloda.foglalas(szobaszam=202, datum="2024-05-26")
    szalloda.foglalas(szobaszam=202, datum="2024-05-24")  # próbáljuk meg ismételten foglalni ugyanarra a dátumra

    szalloda.foglalasok_listazasa()

    szalloda.lemondas(szobaszam=201, datum="2024-05-25")
    szalloda.lemondas(szobaszam=101, datum="2024-05-26")  # próbáljuk meg törölni egy nem létező foglalást

if __name__ == "__main__":
    main()
