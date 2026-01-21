import sqlite3
from film import *
from film_gui import FilmGui

db_path="film.db"

conn=sqlite3.connect(db_path)
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS film
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    nev      VARCHAR(50),
    kiadas   INTEGER,
    rendezo  VARCHAR(50),
    mufaj    VARCHAR(50),
    megnezve INTEGER
);
""")

conn.commit()






root=FilmGui(db_path)
film_database=FilmDatabase(db_path)


root.together("Név","Kiadás Dátuma(évben)", "Rendező", "Műfaj")

root.mainloop()
