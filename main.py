# Beadandó: Szálloda foglalási rendszer

from hotel import Szalloda, EgyagyasSzoba, KetagyasSzoba
import datetime

def main_menu(szalloda):
    while True:
        print("\nÜdvözöljük a Szálloda Foglalási Rendszerében!")
        print("Válasszon az alábbi opciók közül:")
        print("1 - Szoba foglalása")
        print("2 - Foglalás lemondása")
        print("3 - Összes foglalás listázása")
        print("4 - Kilépés")
        
        valasztas = input("Kérem adja meg a választott opció számát: ")
        
        if valasztas == "1":
            foglalas_hozzaadasa(szalloda)
        elif valasztas == "2":
            foglalas_torlese(szalloda)
        elif valasztas == "3":
            print(szalloda.foglalasok_listazasa())
        elif valasztas == "4":
            print("Köszönjük, hogy igénybe vette szolgáltatásainkat!")
            break
        else:
            print("Érvénytelen választás, kérem próbálja újra!")

def foglalas_hozzaadasa(szalloda):
    try:
        szobaszam = input("Adja meg a szobaszámot: ")
        ev = int(input("Adja meg az évet (pl. 2024): "))
        ho = int(input("Adja meg a hónapot (pl. 5): "))
        nap = int(input("Adja meg a napot (pl. 20): "))
        datum = datetime.date(ev, ho, nap)
        ar = szalloda.szoba_foglalas(szobaszam, datum)
        print(f"A foglalás sikeres! Az ár {ar} Ft.")
    except Exception as e:
        print(e)

def foglalas_torlese(szalloda):
    try:
        szobaszam = input("Adja meg a szobaszámot, amelyik foglalást törölni szeretné: ")
        ev = int(input("Adja meg az évet (pl. 2024): "))
        ho = int(input("Adja meg a hónapot (pl. 5): "))
        nap = int(input("Adja meg a napot (pl. 20): "))
        datum = datetime.date(ev, ho, nap)
        uzenet = szalloda.foglalas_lemondas(szobaszam, datum)
        print(uzenet)
    except Exception as e:
        print(e)

szalloda = Szalloda("GDE Hotel")
szalloda.szoba_hozzaadas(EgyagyasSzoba(15000, "101"))
szalloda.szoba_hozzaadas(KetagyasSzoba(20000, "102"))
szalloda.szoba_hozzaadas(EgyagyasSzoba(18000, "103"))

mai_nap = datetime.date.today()
foglalasi_datumok = [mai_nap + datetime.timedelta(days=i) for i in range(1, 6)]

for i, datum in enumerate(foglalasi_datumok):
    szobaszam = "101" if i % 3 == 0 else "102" if i % 3 == 1 else "103"
    try:
        szalloda.szoba_foglalas(szobaszam, datum)
        print(f"Foglalás létrehozva: Szobaszám {szobaszam}, Dátum: {datum}")
    except Exception as e:
        print(f"Hiba történt a foglalás létrehozásakor: {e}")

# A főmenü indítása
if __name__ == "__main__":
    main_menu(szalloda)
