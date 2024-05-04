## Szálloda foglalási rendszer
[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) ![version](https://img.shields.io/badge/version-1.0.0-red)

#### Gábor Dénes Egyetem

###### Készítette: Mohácsi Olivér (IRSQO2)

##### A program az alábbi feladatok alapján készült:

**Osztályok létrehozása:**

- Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám)
- Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.
- Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.)
- Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól)

**Foglalások kezelése:**

- Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát.
- Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását.
- Implementálj egy metódust, ami listázza az összes foglalást.

**Felhasználói interfész és adatvalidáció:**

- Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás).
- A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor.
- Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek.
- Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik.
