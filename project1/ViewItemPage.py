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
              AddOnItem("Packing Peanuts", 35.00)]

    def __init__(self, master=None, *args, **kwargs):
        # configure page
        Page.__init__(self, *args, **kwargs)
        self.cart = ViewCartPage()

        # Set breadcrumb frame
        self.label = tk.LabelFrame(
            self, text="Store > View Item", padx=10, pady=10)
        self.label.pack(side="top", fill="both", expand=True)

        # configure grid weights (resize)
        self.label.grid_columnconfigure(0, weight=1)
        self.label.grid_columnconfigure(1, weight=1)
        self.label.grid_columnconfigure(2, weight=1)
        self.label.grid_columnconfigure(3, weight=1)
        self.label.grid_columnconfigure(4, weight=1)
        self.label.grid_columnconfigure(5, weight=1)
        self.label.grid_columnconfigure(6, weight=1)
        self.label.grid_columnconfigure(7, weight=1)
        self.label.grid_columnconfigure(8, weight=1)
        self.label.grid_columnconfigure(9, weight=1)
        self.label.grid_columnconfigure(10, weight=1)
        self.label.grid_columnconfigure(11, weight=1)

        # Set nav buttons
        tk.Button(self.label, text='Back to Store', width=15,
                  command=self.hide).grid(row=0, column=0, columnspan=2, sticky="nw")
        tk.Button(self.label, text='Cart', width=15,
                  command=self.ViewCartPageNav).grid(row=0, column=10, columnspan=2, sticky="ne")

        # Set Main Image
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        imgPath = imagesPath / "bluebox.png"
        img = tk.PhotoImage(file=rf"{imgPath}")
        mainImage = tk.Label(self.label, image=img)
        mainImage.image = img
        mainImage.grid(row=0, column=2, columnspan=8)

    def sendBox(self, box):
        # Set box instance
        self.box = Box(box.name, box.price, box.image, box.description)
        boxItem = tk.Label(self.label, image=box.image)
        boxItem.image = box.image
        boxItem.grid(row=1, column=0, columnspan=3, rowspan=5)

        # Set Product Name
        tk.Label(self.label, text=box.name,
                 font="Helvetica 28 bold").grid(row=1, column=3, columnspan=3, sticky="w")

        # Set Product price
        tk.Label(self.label, text="Price ",
                 font="Helvetica 20 bold").grid(row=2, column=3, sticky="w")
        tk.Label(self.label, text="$"+"{:.2f}".format(box.price)+"/ea",
                 font="Helvetica 20").grid(row=2, column=4, columnspan=2, sticky="w")

        # Set stock status
        tk.Label(self.label, text="In Stock",
                 fg="dark green", font="Helvetica 20 bold").grid(row=3, column=3, columnspan=3, sticky="w")

        # Set product description
        tk.Label(self.label, text=str(box.description), font="Helvetica 18", wraplength=500, justify="left").grid(
            row=4, column=3, columnspan=3, rowspan=4, sticky="nw")

        # Quantity spinbox
        tk.Label(self.label, text="Quantity", font="Helvetica 18").grid(
            row=1, column=7, sticky="w")

        self.boxQ = tk.IntVar()
        self.boxQ.set(box.quantity)
        self.spinBox = tk.Spinbox(
            self.label, from_=1, to=2500, textvariable=self.boxQ)
        self.spinBox.grid(row=1, column=8, columnspan=2)

        # Add-ons
        tk.Label(self.label, text="Add-ons", font="Helvetica 18").grid(
            row=2, column=7, sticky="w")

        # Issue with background color. Cant find a way to change it -AS
        self.vars = []
        row = 3
        for pick in self.addOns:
            var = tk.IntVar()
            chk = ttk.Checkbutton(
                self.label, text=pick.name + " $" + "{:.2f}".format(pick.price), variable=var, style="SE.TCheckbutton")
            chk.grid(row=row, column=7, columnspan=3, sticky="w", pady=5)
            row += 1
            self.vars.append(var)

        # Add to cart button
        tk.Button(self.label, text="Add Item to Cart", font="Helvetica 18",
                  command=self.addToCart, width=15).grid(row=row+2, column=7, columnspan=2, sticky="w", pady=(20, 0))

    # clear out the box
    def clearBox(self):
        self.box = None

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
