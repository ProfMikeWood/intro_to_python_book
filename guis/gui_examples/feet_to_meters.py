
# this is a GUI to convert feet to meters

# import the tkinter module
from tkinter import *
from tkinter import ttk

# create a FeetToMeters class
class FeetToMeters:

    # define the init method of the class
    def __init__(self, root):

        # add a title to the window
        root.title("Unit Conversion")

        # add a main frame and add it to the window
        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)

        # define two string variables for feet and meters
        self.feet = StringVar()
        self.meters = StringVar()

        # create an Entry widget that is bound to the feet string variable
        # and add it to row 1 and column 2 of the main frame
        feet_entry = ttk.Entry(mainframe, textvariable=self.feet)
        feet_entry.grid(column=2, row=1)

        # add Labels showing showing the text as organized in 
        # the format shown in the class handout
        ttk.Label(mainframe,text="feet").grid(column=3, row=1)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2)
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2)

        # add a Button with the word "Calculate"
        # bind the button to the calculate function
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3)

    # write a function called calculate
    # get the feet variable and try converting to a float
    # if it works, then convert the value to meters and assign
    # to the meters string variable with 4 decimal places
    # 1 foot = 0.3048 meters
    # if it's not convetable to a float, do nothing
    def calculate(self):
        try:
            value = float(self.feet.get())
            self.meters.set('{:.2f}'.format(value*0.3048))
        except ValueError:
            pass

# create a root Tk object
root = Tk()

# create a FeetToMeters object with the Tk root object as an argument
FeetToMeters(root)

# call the mainloop method on the Tk root object
root.mainloop()



