import tkinter as tk
from tkinter import ttk
from ViewCartPage import ViewCartPage
from page import Page
from box import Box
from addOnItem import AddOnItem
from pathlib import Path    # Handing cross-platform paths
import os


class ViewItemPage(Page):
    # define all of the add-on items and prices
    addOns = [AddOnItem("Packing Tape", 4.50),
              AddOnItem("Packing Wrap", 15.00),
              AddOnItem("Packing Bags", 10.00),
              AddOnItem("Shipping Labels", 9.00),
              AddOnItem("Bubble Wrap", 25.00),
              AddOnItem("Packing Peanuts", 35.00)
              ]

    def __init__(self, master=None, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.cart = ViewCartPage()

        # Set breadcrumb frame
        self.label = tk.LabelFrame(self, text="Store > View Item")
        self.label.pack(side="top", fill="both", expand=True)

        # Set Main Image
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        imgPath = imagesPath / "bluebox.png"
        img = tk.PhotoImage(file=rf"{imgPath}")

        mainImage = tk.Label(self.label, image=img)
        mainImage.image = img
        mainImage.grid(row=0, column=2, padx=100, rowspan=6, columnspan=2)
        tk.Button(self.label, text='Cart', command=self.ViewCartPageNav).grid(
            row=0, column=4, sticky="n")
        tk.Button(self.label, text='Back to Store', command=self.hide).grid(
            row=0, column=0, sticky=(tk.N + tk.W))

    def sendBox(self, box):
        # Set box instance
        self.box = Box(box.description, box.price, box.image)
        boxItem = tk.Label(self.label, image=box.image)
        boxItem.image = box.image
        boxItem.grid(row=6, column=1, rowspan=5)

        # Set Product Name TODO: Change to name
        tk.Label(self.label, text=box.description,
                 font="Helvetica 28 bold").grid(row=6, column=2)

        # Set Product price
        tk.Label(self.label, text="Price ",
                 font="Helvetica 20 bold").grid(row=7, column=2)
        tk.Label(self.label, text="$"+str(box.price)+"/ea",
                 font="Helvetica 20").grid(row=7, column=3)

        # TODO: Set product description

        # Set stock status
        tk.Label(self.label, text="In Stock",
                 fg="light green", font="Helvetica 16 bold").grid(row=8, column=2)

        # Quantity spinbox
        self.boxQ = tk.IntVar()
        self.boxQ.set(box.quantity)
        self.boxQ.trace_add("write", self.updateQuantity)
        self.spinBox = tk.Spinbox(
            self.label, from_=1, to=2500, textvariable=self.boxQ)
        self.spinBox.grid(column=4, row=6)

        # Add-ons
        self.vars = []
        row = 7
        for pick in self.addOns:
            var = tk.IntVar()
            chk = ttk.Checkbutton(
                self.label, text=pick.name + " $" + str(pick.price), variable=var)
            chk.grid(row=row, column=4)
            row += 1
            self.vars.append(var)

        # Add to cart button
        tk.Button(self.label, text="Add Item to Cart",
                  command=self.addToCart).grid(row=row+2, column=4)

    # clear out the box
    def clearBox(self):
        self.box = None

    # Update quantity trace
    def updateQuantity(self, *args):
        print("quantity updated")  # idk just need something here

    # Add item to the cart
    def addToCart(self):
        count = 0
        for var in self.vars:
            if(var.get() == 1):
                self.box.addOns.append(self.addOns[count])
                count += 1
        self.box.quantity = self.boxQ.get()
        self.cart.addItemToCart(self.box)
        self.hide()

    # Nav to ViewCart page
    def ViewCartPageNav(self):
        self.hide()
        self.master.ViewCartPageNav()
