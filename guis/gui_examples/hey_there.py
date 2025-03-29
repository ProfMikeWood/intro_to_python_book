
# this is a GUI to show a simple label

# import tkinter
from tkinter import *
from tkinter import ttk

# define a class called HeyThere
class HeyThere:

    # define an __init__ method with root as an argument
    def __init__(self, root):

        # add a title to the GUI
        root.title("Greetings from Tkinter")

        # add a Label to the GUI
        label = ttk.Label(root, text="What's Up", width=30, justify='center')

        # use the grid method to add the label to the GUI
        label.grid(column=0, row=0)
        

# create a root Tk object
root = Tk()

# create a HeyThere object with the Tk root object as an argument
HeyThere(root)

# call the mainloop method on the Tk root object
root.mainloop()




