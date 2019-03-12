import tkinter as tk
from page import Page
import os
from pathlib import Path    # Handing cross-platform paths


class ViewCartPage(Page):
    cart = []

    def __init__(self, master=None, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Set breadcrumb frame
        self.label = tk.LabelFrame(
            self, text="Store > View Cart", padx=10, pady=10)
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

        # Set Main Image
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        imgPath = imagesPath / "bluebox.png"
        img = tk.PhotoImage(file=rf"{imgPath}")
        mainImage = tk.Label(self.label, image=img)
        mainImage.image = img
        mainImage.grid(row=0, column=2, columnspan=8)

        # Show Discount offers
        tk.Label(self.label, text='Orders of more than 50 boxes ship FREE', fg="dark red", font="Helvetica 20 bold").grid(
            row=1, column=2, columnspan=8)
        tk.Label(self.label, text='Apply a 10% discount with a purchase of 150 boxes or more', fg="dark red", font="Helvetica 20 bold").grid(
            row=2, column=2, columnspan=8)

        if(len(self.cart) > 0):
            # display cart contents
            currentRow = 3
            total = 0.0
            for box in self.cart:
                # set product image
                boxItem = tk.Label(self.label, image=box.imageSm)
                boxItem.image = box.imageSm
                boxItem.grid(column=0, columnspan=3,
                             row=currentRow, rowspan=2)

                # Set Product Name
                tk.Label(self.label, text=box.name,
                         font="Helvetica 15 bold").grid(row=currentRow, column=3, columnspan=3, sticky="w")

                # Set Product price
                tk.Label(self.label, text="Price ",
                         font="Helvetica 15 bold").grid(row=currentRow+1, column=3, sticky="w")
                tk.Label(self.label, text="$"+"{:.2f}".format(box.price)+"/ea",
                         font="Helvetica 15").grid(row=currentRow+1, column=4, columnspan=2, sticky="w")

                # show addons
                tk.Label(self.label, text=self.getAddOns(
                    box)).grid(column=3, row=currentRow+2, sticky="w")

                # show quantity of boxes
                tk.Label(self.label, text="Quantity: " + str(box.quantity)
                         ).grid(column=9, row=currentRow, sticky="e")
                total += self.getBoxTotal(box)
                currentRow += 2

            # display totoal
            tk.Label(self.label, text="Total: $" +
                     "{:.2f}".format(total)).grid(column=5, row=currentRow, sticky="e")

            # checkout button
            tk.Button(self.label, text='Checkout', command=self.ViewCheckoutPageNav).grid(
                row=currentRow+1, column=5, sticky="e")
        else:
            # display empty cart message
            tk.Label(self.label, text='Your cart is empty!', font="Helvetica 25 bold").grid(
                row=3, column=5, columnspan=2, pady=(30, 0))
            tk.Button(self.label, text='Back to Store', width=15,
                      command=self.hide).grid(row=4, column=5, columnspan=2)

    def addItemToCart(self, newBox):
        found = False
        if(len(self.cart) == 0):
            self.cart.append(newBox)
        else:
            for box in self.cart:
                if(box.name == newBox.name):
                    box.quantity = newBox.quantity
                    box.addOns = list(newBox.addOns)
                    found = True
            if(found == False):
                self.cart.append(newBox)

    def clearCart(self):
        self.cart.clear()

    def getAddOns(self, box):
        addOnList = "Add-on items: "
        if(len(box.addOns) == 0):
            addOnList += "None"
        else:
            count = 0
            for addOn in box.addOns:
                if(count > 0):
                    addOnList += ", "
                if(count > 1):
                    count = 0
                    addOnList += "\n"
                addOnList += " " + addOn.name + \
                    "($" + "{:.2f}".format(addOn.price) + ")"
                count += 1
        return addOnList

    def getBoxTotal(self, box):
        total = 0.0
        for addOn in box.addOns:
            total += addOn.price
        total += box.price * box.quantity
        return total

    def getNumBoxes(self):
        total = 0
        for box in self.cart:
            total += box.quantity
        return total

    def ViewCheckoutPageNav(self):
        self.hide()
        self.master.ViewCheckoutPageNav()
