# A hotel.py file tartalmazza a Szoba, EgyagyasSzoba, KetagyasSzoba, Szalloda és Foglalas osztályokat.

from abc import ABC, abstractmethod
import datetime

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_ar(self):
        pass

class EgyagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)
        self.foglalasok[szoba.szobaszam] = []

    def szoba_foglalas(self, szobaszam, datum):
        if datum <= datetime.date.today():
            raise ValueError("A foglalás dátuma nem lehet a mai napnál korábbi.")
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum not in self.foglalasok[szobaszam]:
                    self.foglalasok[szobaszam].append(datum)
                    return szoba.get_ar()
                else:
                    raise ValueError("Ez a szoba ezen a napon már foglalt.")
        raise ValueError("Nem létező szobaszám.")

    def foglalas_lemondas(self, szobaszam, datum):
        if datum <= datetime.date.today():
            raise ValueError("Múltbeli vagy mai napi foglalás nem mondható le.")
        if szobaszam in self.foglalasok and datum in self.foglalasok[szobaszam]:
            self.foglalasok[szobaszam].remove(datum)
            return f"A foglalás sikeresen lemondva a(z) {szobaszam} számú szobára, dátum: {datum}."
        else:
            raise ValueError("A megadott szobához és dátumhoz nincs foglalás.")

    def foglalasok_listazasa(self):
        foglalas_lista = []
        for szobaszam, datumok in self.foglalasok.items():
            for datum in sorted(datumok):
                foglalas_lista.append(f"Szobaszám: {szobaszam}, Dátum: {datum}")
        if not foglalas_lista:
            return "Jelenleg nincsenek foglalások."
        return "\n".join(foglalas_lista)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def get_ar(self):
        return self.szoba.get_ar()
