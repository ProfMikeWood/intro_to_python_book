# a GUI to add two numbers

# import the tkinter package
from tkinter import *
from tkinter import ttk

# create a class called AddReturn
class AddReturn:

    # add an init functions for this class
    def __init__(self, root):

        # Add a title to the window
        root.title("Sum of Two Numbers")

        # Define the geometry of the window
        root.geometry("300x200")

        # Configure the root so that it stretches in all directions
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Add a mainframe which is sticky in all directions
        # Add some padding (e.g. 5 pixels) to the frame
        mainframe = ttk.Frame(root, padding = "5 5 5 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # weight column to expand with the window
        mainframe.columnconfigure(0, weight=1)

        # Define three variables for the first number,
        # the second number, and the sum of the two numbers
        self.x = StringVar()
        self.y = StringVar()
        self.sum = StringVar()

        # add a Label for the first number
        label = Label(mainframe, text="Enter your first number:",
                      font=('Arial',20))
        label.grid(row=0, column=0, sticky=(W,E))

        # add an Entry for the first number
        entry_1 = Entry(mainframe, textvariable=self.x,
                      font=('Arial',20))
        entry_1.grid(row=1, column=0, sticky=(W,E), columnspan=2)

        # bind the Return key to the first Entry box
        entry_1.bind('<Return>', self.return_action)

        # add a Label for the second number
        label = Label(mainframe, text="Enter your second number:",
                      font=('Arial',20))
        label.grid(row=2, column=0, sticky=(W,E))

        # add an Entry for the second number
        entry_2 = Entry(mainframe, textvariable=self.y,
                      font=('Arial',20))
        entry_2.grid(row=3, column=0, sticky=(W,E))

        # bind the Return key to the second Entry box
        entry_2.bind('<Return>', self.return_action)

        # add a Label for the sum of the numbers
        label = Label(mainframe, text="The sum of your numbers:",
                      font=('Arial',20))
        label.grid(row=4, column=0, sticky=(W,E))

        # add an Entry for the sum of the numbers
        entry_3 = Entry(mainframe, textvariable=self.sum,
                      font=('Arial',20))
        entry_3.grid(row=5, column=0, sticky=(W,E))

        # bind the Return key to the sum Entry box
        entry_3.bind('<Return>', self.return_action)

    # define a return_action function that can be called 
    # when a given event occurs
    # function should try to add the two numbers
    # if they can't be added (e.g. because one is not a float)
    # then return NaN
    def return_action(self, event):
        try:
            x_plus_y = str(float(self.x.get())+float(self.y.get()))
            self.sum.set(x_plus_y)
        except:
            self.sum.set('NaN')

# create a root Tk object
root = Tk()

# create an AddReturn object with the Tk root object as an argument
AddReturn(root)

# call the mainloop method on the Tk root object
root.mainloop()