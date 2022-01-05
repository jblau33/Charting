from tkinter import *
#from PIL import ImageTK, Image
from PIL import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title = ("TKinter Charting Exercise")
root.iconbitmap ("C:\pythonprojects\charting\camera.ico")
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(200000,25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text = "graph it!", command = graph)
my_button.pack()
root.mainloop()





