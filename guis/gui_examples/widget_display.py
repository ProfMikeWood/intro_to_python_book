
# this is a GUI to showcase a few of the widgets in tkinter

# improt tkinter
from tkinter import *
from tkinter import ttk

# define a class called WidgetDisplay
class WidgetDisplay:

    # define an __init__ method with root as an argument
    def __init__(self, root):

        # add a title for the GUI
        root.title("Widget Showcase")

        # add a frame to the GUI
        first_frame = ttk.Frame(root)
        first_frame.grid(column=0, row=0)

        # add a label to the first frame and add it to the GUI
        label = ttk.Label(first_frame, text="Choose an option")
        label.grid(column=0, row=0)

        # add a ComboBox to the first frame and add it to the GUI
        label = ttk.Combobox(first_frame, values=['Option 1','Option 2','Option 3'])
        label.grid(column=0, row=1)

        # add a second frame to the GUI
        second_frame = ttk.Frame(root)
        second_frame.grid(column=1, row=0)

        # add a label to the second frame and add it to the GUI
        label = ttk.Label(second_frame, text="Enter your name")
        label.grid(column=0, row=0)

        # add an Entry to the second frame and add it to the GUI
        label = ttk.Entry(second_frame)
        label.grid(column=0, row=1)

        # add a Button to the second frame and add it to the GUI
        label = ttk.Button(second_frame, text="Enter")
        label.grid(column=0, row=2)
        

# create a root Tk object
root = Tk()

# create a WidgetDisplay object with the Tk root object as an argument
WidgetDisplay(root)

# call the mainloop method on the Tk root object
root.mainloop()




