import sqlite3

class FilmDatabase:

    def __init__(self,database):
        self.conn=sqlite3.connect(database)
        self.cursor=self.conn.cursor()


    def insert_users(self,name: str, release_year: int, director: str, genre: str, watched: int = 0):

        try:
            self.cursor.execute("INSERT INTO film(nev,kiadas,rendezo,mufaj,megnezve) VALUES (?,?,?,?,?)", (name, release_year, director, genre, watched))
            self.conn.commit()
        except sqlite3.DatabaseError as e:
            print(f"There was an error with the database {e}")

    def show_all(self):
        self.cursor.execute("SELECT * from film")
        rows = self.cursor.fetchall()
        return rows

    def delete_rows_with_param(self,param):
        self.cursor.execute("DELETE FROM film WHERE nev LIKE ?",(param,))