import tkinter as tk
from page import Page
import os
from pathlib import Path    # Handing cross-platform paths


class ViewCartPage(Page):
    cart = []

    def __init__(self, master=None, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Set breadcrumb frame
        label = tk.LabelFrame(self, text="Store > View Cart")
        label.pack(side="top", fill="both", expand=True)

        # Set Main Image
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        imgPath = imagesPath / "bluebox.png"
        img = tk.PhotoImage(file=rf"{imgPath}")

        mainImage = tk.Label(label, image=img)
        mainImage.image = img
        mainImage.grid(row=0, column=1, padx=100, rowspan=6, columnspan=3)
        tk.Button(label, text='Back to Store',
                  command=self.hide).grid(column=0, row=0)
        if(len(self.cart) > 0):
            row = 7
            total = 0.0
            for box in self.cart:
                boxItem = tk.Label(label, image=box.image)
                boxItem.image = box.image
                boxItem.grid(column=0, row=row, rowspan=2)
                tk.Label(label, text=box.description + "\n" +
                         "$" + str(box.price) + "/ea").grid(column=1, row=row)
                tk.Label(label, text=self.getAddOns(
                    box)).grid(column=1, row=row+1)
                tk.Label(label, text="Quantity: " + str(box.quantity)
                         ).grid(column=5, row=row, sticky="e")
                total += self.getBoxTotal(box)
                row += 2
            tk.Label(label, text="Total: $" +
                     "{:.2f}".format(total)).grid(column=5, row=row, sticky="e")
            tk.Button(label, text='Checkout', command=self.ViewCheckoutPageNav).grid(
                row=row+1, column=5, sticky="e")
        else:
            tk.Label(label, text='Cart is empty!').grid(
                row=7, column=2, columnspan=5)

    def addItemToCart(self, newBox):
        found = False
        if(len(self.cart) == 0):
            self.cart.append(newBox)
        else:
            for box in self.cart:
                if(box.description == newBox.description):
                    box.quantity = newBox.quantity
                    box.addOns = list(newBox.addOns)
                    found = True
            if(found == False):
                self.cart.append(newBox)

    def clearCart(self):
        self.cart.clear()

    def getAddOns(self, box):
        addOnList = "Add on items: "
        if(len(box.addOns) == 0):
            addOnList += "None"
        else:
            count = 0
            for addOn in box.addOns:
                if(count > 1):
                    count = 0
                    addOnList += "\n"
                addOnList += " " + addOn.name
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
