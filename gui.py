import tkinter as tk
from army import Units, Order, Army
from ann50 import ann50


starter = tk.Tk()

class Gamewindow:

def mnarmy():
   arwindow = tk.Toplevel()
def initmain(game):
   root = tk.Tk()
   mnarmybut = tk.Button(root, text="Make new army", command=mnarmy)
   mnarmybut.pack()
def ann50init():
   game = ann50()
   starter.destroy()
   initmain(game)
slabel = tk.Label(starter, text="Choose game edition")
slabel.pack()
ann50but = tk.Button(starter, text='50th Anniversary Edition', command=ann50init)
ann50but.pack()
starter.mainloop()
