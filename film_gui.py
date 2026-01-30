from tkinter import *
from tkinter import ttk
from types import new_class

from film import *

class FilmGui:
    def __init__(self,database):

        self.mufaj_var = None
        self.rendezo_var = None
        self.datum_var = None
        self.nev_var = None
        self.check = None

        self.root=Tk()
        self.root.title("Film Database")
        self.root.geometry("500x400")
        self.mainframe=ttk.Frame(self.root)
        self.mainframe.grid(column=0,row=0)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.film=FilmDatabase(database)

    def main_window(self):

        self.nev_var=StringVar()
        self.datum_var=StringVar()
        self.rendezo_var = StringVar()
        self.mufaj_var = StringVar()

        ttk.Label(self.mainframe,text="Adja meg a filmnek az adatait",padding=(10,10)).grid(column=1,columnspan=2,row=0)

        ttk.Entry(self.mainframe,textvariable=self.nev_var).grid(column=1,row=1,pady=10)
        ttk.Label(self.mainframe,text="Név").grid(column=2,row=1)

        ttk.Entry(self.mainframe,textvariable=self.datum_var).grid(column=1,row=2,pady=10)
        ttk.Label(self.mainframe,text="Kiadás Dátuma(évben)").grid(column=2,row=2,padx=10)

        ttk.Entry(self.mainframe,textvariable=self.rendezo_var).grid(column=1,row=3,pady=10)
        ttk.Label(self.mainframe,text="Rendező").grid(column=2,row=3)

        ttk.Entry(self.mainframe,textvariable=self.mufaj_var).grid(column=1,row=4,pady=10)
        ttk.Label(self.mainframe,text="Műfaj").grid(column=2,row=4)

        self.check=BooleanVar()
        ttk.Checkbutton(self.mainframe,text="Megnézve",variable=self.check).grid(column=2,row=5,columnspan=2)

        ttk.Button(self.mainframe,text="Insert Film",command=lambda:self.film.insert_users(*self.put_film_vars_to_list())).grid(column=0,columnspan=2,row=6)

        ttk.Button(self.mainframe, text="Film keresése",command=lambda :self.search_window()).grid(column=1, row=7)

        ttk.Button(self.mainframe,text="Film törlése",command=lambda :self.delete_window()).grid(column=2,row=7)

    def put_film_vars_to_list(self):
        film_list=[]
        for i in (self.nev_var,self.datum_var,self.rendezo_var,self.mufaj_var,self.check):
            film_list.append(i.get())
            i.__del__()
        self.check.set(value=0)
        return film_list

    def mainwindow_button(self):
        ttk.Button(self.mainframe,text="Listázd az összes filmet",command=lambda :self.show_all_window(self.film.show_all())).grid(column=2,columnspan=2,row=6)

    def show_all_window(self,inputted):
        new_window=Toplevel()
        new_window.geometry("600x500")
        new_window.title("Az összes film listázva")

        new_window.columnconfigure(0, weight=1)
        new_window.rowconfigure(0, weight=1)

        tree = ttk.Treeview(
            new_window,
            columns=("id","nev", "kiadas", "rendezo","mufaj","megnezve"),
            show="headings"
        )

        columns = {
            "id": "ID",
            "nev": "Név",
            "kiadas": "Kiadás",
            "rendezo": "Rendező",
            "mufaj": "Műfaj",
            "megnezve": "Megnézve"
        }

        for col, text in columns.items():
            tree.heading(col, text=text)
            tree.column(col, anchor="center", width=100)

        tree.grid(column=0, row=0, sticky="nesw")
        rows=inputted
        for i in rows:
            tree.insert("","end",values=i)

        ttk.Button(new_window,text="Vissza",command=lambda :new_window.destroy()).grid(column=0,row=2,pady=100)

    def search_window(self):
        new_window=Toplevel()
        new_window.title("Film keresése")
        new_window.geometry("500x500")
        new_window.columnconfigure(0,weight=1)
        new_window.columnconfigure(1,weight=2)
        new_window.rowconfigure(0,weight=1)
        new_window.rowconfigure(1,weight=2)

        search_entry=StringVar()
        ttk.Entry(new_window,textvariable=search_entry).grid(column=0,row=0,sticky="e",padx=50)
        combo = ttk.Combobox(new_window, values=["Név", "Rendező", "Műfaj"],state="readonly")
        combo.grid(column=1,row=0)
        combo.set("Válassz")

        ttk.Button(new_window,text="Keresés",command=lambda :self.show_all_window(self.film.show_by_name(self.__combobox_helper(combo),search_entry.get()))).grid(column=0,row=1)
        ttk.Button(new_window,text="Vissza",command=lambda :new_window.destroy()).grid(column=1,row=1)

    def __combobox_helper(self,combo):
        combo_value=combo.get()
        value = ""
        if combo_value == "Rendező":
            value = "rendezo"
        elif combo_value == "Név":
            value = "nev"
        elif combo_value == "Műfaj":
            value = "mufaj"
        return value

    def delete_window(self):
        new_window=Tk()
        new_window.geometry("500x500")
        new_window.title("Film törlése")
        new_window.columnconfigure(0,weight=1)
        new_window.columnconfigure(1,weight=1)
        new_window.rowconfigure(0,weight=1)
        new_window.rowconfigure(1,weight=1)

        delete_entry=StringVar()
        ttk.Entry(new_window,textvariable=delete_entry).grid(column=0,row=0)
        combo=ttk.Combobox(new_window,values=["Név","Műfaj"],state="readonly")
        combo.grid(column=1,row=0)
        combo.set("Válassz")

        ttk.Button(new_window,text="Vissza",command=lambda :new_window.destroy()).grid(column=0,row=1)
        ttk.Button(new_window,text="Film törlése",command=lambda :self.film.delete_combined(self.__combobox_helper(combo),delete_entry.get())).grid(column=1,row=1)

    def together(self):
        self.main_window()
        self.mainwindow_button()

    def mainloop(self):
        self.root.mainloop()