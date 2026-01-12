import sqlite3
from film import *

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


film_database=FilmDatabase(db_path)

film_database.delete_rows_with_param("Eredet")

film_database.insert_users("Eredet",2012,"Christopher Nolan","Sci-Fi",1)

films=film_database.show_all()

print(films)





