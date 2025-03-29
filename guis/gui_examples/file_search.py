
# a GUI to demo a file menu

# import the tkinter package
from tkinter import *
from tkinter import ttk

# import the 
from tkinter.filedialog import askopenfilename

# import the os module
import os

# create a class called PopupWindows
class PopupWindows:

    # add an init functions for this class
    def __init__(self, root):

        # Add a title to the window
        root.title("Window with File Menu")

        # Define the geometry of the window
        root.geometry("500x200")

        # Make a variable for the file name
        self.chosen_file = StringVar(value='None Chosen Yet')

        # add a Menu to to the window
        menubar = Menu(root)

        # add a file drop-down menu from the top bar with label File
        # add labels for New, Open, Save, and Exit
        # use a choose_file function for Open and a quit function for Exit
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=self.choose_file)
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        # Configure the root so that it stretches in all directions
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # make a frame for the GUI
        self.frame = ttk.Frame(root, padding = "10 10 10 10")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # weight column to expand with the window
        self.frame.columnconfigure(0, weight=1)

        # add a label for the new window
        label = ttk.Label(self.frame,
                          text="Chosen File",
                          font=('Arial',20))
        label.grid(column=0, row=0, sticky=(N, W, E, S))

        # add a label for the chosen file
        label = ttk.Label(self.frame,
                          textvariable=self.chosen_file,
                          font=('Arial',20))
        label.grid(column=0, row=1, sticky=(N, W, E, S))

    # define a choose_file function to find a file
    # in the file system with the askopenfilename function
    def choose_file(self):
        file_name = askopenfilename(initialdir = os.getcwd())
        file_name = os.path.basename(file_name)
        self.chosen_file.set(file_name)

# create a root Tk object
root = Tk()

# create a PopupWindows object with the Tk root object as an argument
PopupWindows(root)

# call the mainloop method on the Tk root object
root.mainloop()