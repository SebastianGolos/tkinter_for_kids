from tkinter import *
import random

colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]

def change_color():
    random_color = random.choice(colors)
    my_window.configure(bg=random_color)

my_window = Tk()
my_window.title("Color Game")
my_window.geometry("500x200")

start_button = Button(text = "Press me!", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady = 10, command=change_color)
start_button.grid(row=1, column= 1)

my_window.configure(bg="red")

my_window.mainloop()

