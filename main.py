import sqlite3

db_path="film.db"

conn=sqlite3.connect(db_path)
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS film
(
    id       INT PRIMARY KEY,
    nev      VARCHAR(50),
    kiadas   INTEGER,
    rendezo  VARCHAR(50),
    mufaj    VARCHAR(50),
    megnezve INTEGER
);
""")

