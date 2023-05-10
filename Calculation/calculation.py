from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Тест")
root.geometry("600X250-810+300")
root.resizable(0,0)
root['bg'] = "#000"
bth = Button(root, text="Click", bg="red")
bth.pack()

bth2 = ttk.Button(root, text="Clack")
bth2.pack()

root.mainloop()