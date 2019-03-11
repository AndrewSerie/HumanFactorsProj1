import tkinter as tk
from tkinter import ttk
from box import Box
from ViewCartPage import ViewCartPage
from ViewItemPage import ViewItemPage
from CheckoutPage import CheckoutPage
import os
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        scriptDir = os.getcwd()
        squareBox = tk.PhotoImage(file=rf"{scriptDir}\UIProj\box1.png")
        rectangleBox = tk.PhotoImage(file=rf"{scriptDir}\UIProj\box2.png")

        boxes = [Box("8\" Square Box",0.51, squareBox),
                 Box("11\" Square Box",1.22,squareBox),
                 Box("15\" Square Box",1.75,squareBox),
                 Box("12\"x9\"x6\" Rectangle Box",2.37,rectangleBox),
                 Box("14\"x11\"x8\" Rectangle Box",2.99,rectangleBox),
                 Box("16\"x13\"x10\" Rectangle Box",3.44,rectangleBox),
                 ]

        tk.Button(self, text = 'Cart', command= self.ViewCartPageNav).grid(row = 0, column = 2, sticky = "n")
        rowCount = 1
        columnCount = 0
        for box in boxes:
            boxItem = tk.Label(self,image = box.image)
            boxItem.image = box.image
            boxItem.grid(row = rowCount, column = columnCount, padx = 75)
            boxButton = tk.Button(self, command = lambda box = box: self.ViewItemPageNav(box), text = box.description + "\n" + "$" + str(box.price) + "/ea").grid(row = rowCount+1, column = columnCount, padx = 75)
            columnCount = columnCount+1
            if(columnCount > 2):
                columnCount = 0
                rowCount = rowCount+2

    def ViewItemPageNav(self, box):
        viewItemPageRef = ViewItemPage(self,self)
        viewItemPageRef.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        viewItemPageRef.clearBox()
        viewItemPageRef.sendBox(box)
        viewItemPageRef.show()

    def ViewCartPageNav(self):
        viewCartPageRef = ViewCartPage(self,self)
        viewCartPageRef.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        viewCartPageRef.show()

    def ViewCheckoutPageNav(self):
        viewCheckoutPageRef = CheckoutPage(self, self)
        viewCheckoutPageRef.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        viewCheckoutPageRef.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("BlueBox")
    root.wm_geometry("1280x720")
    root.configure(background = "white")
    scriptDir = os.getcwd()
    img = tk.PhotoImage(file=rf"{scriptDir}\UIProj\bluebox.png")
    mainImage = tk.Label(main, image = img)
    mainImage.image = img
    mainImage.grid(row = 0, column = 0, sticky = "n", columnspan = 4)
    menuBar = tk.Menu(main)
    helpMenu = tk.Menu(menuBar, tearoff = 0)
    helpMenu.add_command(label = 'About', underline = 0)
    helpMenu.add_command(label = 'Contact', underline = 0)
    menuBar.add_cascade(label = "Help", menu = helpMenu)
    root.config(menu = menuBar)
    root.mainloop()
