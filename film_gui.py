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

        ttk.Label(self.root,text="Adja meg a filmnek az adatait",padding=(10,10)).grid(columnspan=2,row=0)
        entrys=StringVar()
        for e,i in enumerate(args):
            ttk.Entry(self.mainframe,textvariable=entrys).grid(column=1,row=e+1,padx=10,pady=10)
            ttk.Label(self.mainframe,text=i).grid(column=2,row=e+1)

        ttk.Button(self.root,text="Ok").grid(columnspan=2,pady=20)


    def mainloop(self):
        self.root.mainloop()