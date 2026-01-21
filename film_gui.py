from tkinter import *
from tkinter import ttk
from film import *


class FilmGui:
    def __init__(self,database):
        self.root=Tk()
        self.root.title("Film Database")
        self.root.geometry("500x400")
        self.mainframe=ttk.Frame(self.root)
        self.mainframe.grid(column=0,row=0)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=0)
        self.film=FilmDatabase(database)

    def label_generator(self,*args):

        ttk.Label(self.mainframe,text="Adja meg a filmnek az adatait",padding=(10,10)).grid(column=1,columnspan=2,row=0)

        film_entrys=[]
        variables=[]
        for e,i in enumerate(args):
            entrys=Variable()
            variables.append(entrys)
            entry=ttk.Entry(self.mainframe,textvariable=variables[e]).grid(column=1,row=e+1,padx=10,pady=10)

            ttk.Label(self.mainframe,text=i).grid(column=2,row=e+1)

        check=IntVar(value=0)
        ttk.Checkbutton(self.mainframe,text="Megnézve",variable=check).grid(column=2,row=len(args)+1,columnspan=2)
        film_entrys.append(check.get())
        self.put_films(film_entrys)

    def put_films(self,film_entrys):
        ttk.Button(self.mainframe,text="Insert Film",command=lambda:self.film.insert_users(*film_entrys)).grid(column=0,row=6)

    def mainwindow_button(self):
        ttk.Button(self.mainframe,text="Listázd az összes filmet",command=lambda :self.show_all_window()).grid(column=1,columnspan=2,row=6)


    def show_all_window(self):
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


        tree.grid(column=0, row=0, sticky="new")
        rows=self.film.show_all()
        for i in rows:
            tree.insert("","end",values=i)

        ttk.Button(new_window,text="Vissza",command=lambda :new_window.destroy()).grid(column=0,row=1,pady=100)

    def together(self,*args):

        self.label_generator(*args)
        self.mainwindow_button()

    def mainloop(self):
        self.root.mainloop()

