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

    def show_by_name(self,table_name,variable_name):
        self.cursor.execute(f"SELECT * from film WHERE {table_name} LIKE ?",(variable_name,))
        rows=self.cursor.fetchall()
        print(rows)
        return rows

    def delete_rows_with_param(self,table_name,variable_name):
        query = f"DELETE FROM film WHERE {table_name} LIKE ?"
        self.cursor.execute(query, (f"%{variable_name}%",))
        self.conn.commit()

    def delete_null_rows(self):
        query="DELETE FROM film WHERE nev IS NULL"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_combined(self,table_name,variable_name):
        self.delete_rows_with_param(table_name,variable_name)
        self.delete_null_rows()