import tkinter as tk
from tkinter import *

nombre_planete: int=1

def main():
    espace = tk.Tk()
    espace.geometry("1080x720")
    espace.minsize(720, 480)
    cnv=Canvas(espace, width=1100, height=720, bg="black").pack()
    planetes=[0 for x in range(nombre_planetes)]
    for ii in range(nombre_planetes):
        planetes[ligne] = cnv.create_circle()

    espace.mainloop()



main()




