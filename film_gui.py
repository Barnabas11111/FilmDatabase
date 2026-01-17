from tkinter import *
from tkinter import ttk


class FilmGui:
    def __init__(self):
        self.root=Tk()
        self.root.title("Film Database")
        self.root.geometry("500x400")
        self.mainframe=ttk.Frame(self.root)
        self.mainframe.grid(column=0,row=0)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=0)

    def label_generator(self,*args):

        ttk.Label(self.mainframe,text="Adja meg a filmnek az adatait",padding=(10,10)).grid(column=1,columnspan=2,row=0)
        entrys=StringVar()
        for e,i in enumerate(args):
            ttk.Entry(self.mainframe,textvariable=entrys).grid(column=1,row=e+1,padx=10,pady=10)
            ttk.Label(self.mainframe,text=i).grid(column=2,row=e+1)

    def get_button(self,number):
        ttk.Button(self.mainframe,text="Listázd az összes filmet",command=lambda :self.new_window()).grid(column=1,columnspan=2,row=number)

    def new_window(self):
        new_window=Toplevel()
        new_window.geometry("600x500")
        new_window.title("Az összes film listázva")

        new_window.columnconfigure(0,weight=1)
        new_window.rowconfigure(0,weight=1)


        ttk.Button(new_window,text="Vissza",command=lambda :new_window.destroy()).grid(column=1,row=2)

    def together(self,*args):

        self.label_generator(*args)
        self.get_button(len(args)+1)

    def mainloop(self):
        self.root.mainloop()

