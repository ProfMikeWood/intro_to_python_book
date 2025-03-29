
# this is a GUI to test widget "stickiness"

# import the tkinter module
from tkinter import *
from tkinter import ttk

# create a StickyWidgets class
class StickyWidgets:

    # define the init function
    def __init__(self, root):

        # add a title to the GUI
        root.title("Sticky Widgets")

        # change the style of the root to one of the following:
        #   all platforms: alt, clam, classic, default
        #   Windows: vista, winnative, xpnative
        #   Mac: aqua
        style = ttk.Style(root)
        style.theme_use('clam')

        # configure the root so that it stretches in all directions
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # add a main frame and add it to the window
        # add padding on the main frame
        # make the mainframe sticky in all directions
        # and add it to row 1 and column 2 of the main frame
        mainframe = ttk.Frame(root, padding = "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # configure the mainframe so that it stretches in all directions
        # for rows 0-3 and columns 0-3
        for i in range(4):
            mainframe.columnconfigure(i, weight=1)
            mainframe.rowconfigure(i, weight=1)

        # make an entry widget which is sticky in the W/E directions
        feet_entry = ttk.Entry(mainframe)
        feet_entry.grid(column=0, row=0, sticky = "we",columnspan=4)

        # make labels widgets which are sticky in the W direction
        ttk.Label(mainframe, text='Label 1').grid(column=0, row=1, sticky=W)
        ttk.Label(mainframe,text="Label 2").grid(column=0, row=1, sticky=W)

        # make labels widgets which are sticky in the E direction
        ttk.Label(mainframe, text="Label 3").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="Label 4").grid(column=3, row=2, sticky=E)

        # make a Button widget which is sticky in the S directions
        # and centered in row 3
        ttk.Button(mainframe, text="Button").grid(column=0, row=3, sticky=S, columnspan=4)

        # pad each of the widgets with a pixel size of 5 in both
        # the x and the y directions
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)



# create a root Tk object
root = Tk()

# create a StickyWidgets object with the Tk root object as an argument
StickyWidgets(root)

# call the mainloop method on the Tk root object
root.mainloop()




