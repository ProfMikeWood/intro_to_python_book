# a GUI with some test pop-up windows

# import the tkinter package
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
#import tkinter.font as font

# create a class called PopupWindows
class PopupWindows:

    # add an init functions for this class
    def __init__(self, root):

        # Add a title to the window
        root.title("Pop-Up Windows")

        # Define the geometry of the window
        root.geometry("500x200")

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
                          text="Click this button to open a new window:")
        label.grid(column=0, row=0, sticky=(N, W, E, S))

        # add a button for the new window
        self.button_new_window = ttk.Button(self.frame,
                                       text="New Window",
                                       command=self.another_window)
        self.button_new_window.grid(column=0, row=1, sticky=(N, W, E, S))

        # add a label for the message display
        label = ttk.Label(self.frame,
                          text="Click this button to display a message:")
        label.grid(column=0, row=2, sticky=(N, W, E, S))

        # add a button for the message display
        self.button_showinfo = ttk.Button(self.frame,
                                          text="Show Info",
                                          command=self.showinfo_popup)
        self.button_showinfo.grid(column=0, row=3, sticky=(N, W, E, S))

        # add a label for the closing of the app
        label = ttk.Label(self.frame,
                          text="Click this button to close the application:")
        label.grid(column=0, row=4, sticky=(N, W, E, S))

        # add a button to close the app
        self.button_showinfo = ttk.Button(self.frame,
                                          text="Close",
                                          command=root.destroy)
        self.button_showinfo.grid(column=0, row=5, sticky=(N, W, E, S))


    # define a function to open a new window
    # using a Toplevel object
    # add a label and a button to close the window
    def another_window(self):
        win = Toplevel()
        win.title("Another Window")

        label = ttk.Label(win, text="New widgets go here")
        label.grid(row=0, column=0)

        close_button = ttk.Button(win, text="Close", command=win.destroy)
        close_button.grid(row=1, column=0)


    # define a function to display some info using
    # the showinfo function
    def showinfo_popup(self):
        showinfo("Window", "This window contains some info")


# create a root Tk object
root = Tk()

# create a PopupWindows object with the Tk root object as an argument
PopupWindows(root)

# call the mainloop method on the Tk root object
root.mainloop()
