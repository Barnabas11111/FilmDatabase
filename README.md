# Film Adatbázis Kezelő

Egy Python alapú asztali alkalmazás a személyes filmgyűjtemény kezelésére, amely a grafikus felhasználói felülethez a Tkinter könyvtárat, az adatok helyi tárolásához pedig SQLite adatbázist használ.

## Funkciók
### Film hozzáadása: 
Új filmek rögzítése név, kiadási év, rendező, műfaj és egy megnézett státuszt jelölő jelölőnégyzet (checkbox) segítségével.

### Teljes lista megtekintése: 
Az összes mentett film áttekintése egy tiszta, táblázatos nézetben (ttk.Treeview).

### Keresés: 
Filmek szűrése és keresése név, rendező vagy műfaj alapján egy intuitív lenyíló menü segítségével.

### Film törlése: 
Bejegyzések eltávolítása az adatbázisból név vagy műfaj alapján.

### Helyi SQLite backend: 
Automatikusan létrehozza a strukturált relációs adatbázist az első indítás alkalmával.
