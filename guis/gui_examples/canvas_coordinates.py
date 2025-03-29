# a GUI to return the coordinates of an image
# based on the location of the mouse click

# import the tkinter package
from tkinter import *
from tkinter import ttk

# create a class called CanvasCoords
class CanvasCoords:

    # define an init function
    def __init__(self, root):

        # add a title to the window
        root.title("Canvas Coordinates")

        # change the style
        style = ttk.Style(root)
        style.theme_use('clam')

        # make a frame and stick it to the sides
        mainframe = ttk.Frame(root, padding = "3 3 3 3")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # make variables to store the x and y variables
        self.x = StringVar()
        self.y = StringVar()

        # create an image using a PhotoImage object
        self.img = PhotoImage(file='Canvas_Image.png')

        # add a label and set the image to the photo image object
        self.image_label = ttk.Label(mainframe, image=self.img)
        self.image_label.image = self.img

        # add the Label with the image to the GUI
        self.image_label.grid(column=1, row=2, sticky=(W, E), columnspan=4)

        # bind the primary click button of the mouse click
        self.image_label.bind("<Button-1>", self.mouse_function)

        # make a Label for the x variable
        ttk.Label(mainframe, text='x').grid(column=1, row=4, sticky=(W, E))

        # make an Entry widget for the x variable
        self.x_entry = ttk.Entry(mainframe, width=12, textvariable=self.x)
        self.x_entry.grid(column=2, row=4, sticky = (W, E))

        # make a Label for the y variable
        ttk.Label(mainframe, text='y:').grid(column=3, row=4, sticky=(W, E))

        # make an Entry widget for the y variable
        self.y_entry = ttk.Entry(mainframe, width=12, textvariable=self.y)
        self.y_entry.grid(column=4, row=4, sticky=(W, E))

        # add some padding to each of the widgets
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # create a mouse function 
    def mouse_function(self, event):

        # store the x and y coords of the event to variables
        x = event.x
        y = event.y

        # replace the the Entry widget texts with
        # the new values of x and y
        self.x_entry.delete(0, END)
        self.x_entry.insert(0, x)
        self.y_entry.delete(0, END)
        self.y_entry.insert(0, y)

        # replace the variables with the x and y variables
        self.x.set(x)
        self.y.set(y)


# create a root Tk object
root = Tk()

# create a HeyThere object with the Tk root object as an argument
CanvasCoords(root)

# call the mainloop method on the Tk root object
root.mainloop()

