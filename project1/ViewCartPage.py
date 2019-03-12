import tkinter as tk
from tkinter import ttk
from page import Page
import os
from pathlib import Path    # Handing cross-platform paths


class ViewCartPage(Page):
    cart = []
    cartItems = []

    def __init__(self, master=None, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Set breadcrumb frame
        self.label = tk.LabelFrame(
            self, text="Store > Cart", padx=10, pady=10)
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
        cartDisabled = "normal"
        if (len(self.cart) < 1):
            cartDisabled = "disabled"
        tk.Button(self.label, text='Clear Cart', width=15,
                  command=self.clearCart, state=cartDisabled).grid(row=0, column=10, columnspan=2, sticky="ne")

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

        # setup the cart
        self.setCart()

    def setCart(self):
        self.cartItems.clear()
        if(len(self.cart) > 0):
            # display cart contents
            currentRow = 3
            total = 0.0
            for box in self.cart:
                # set product image
                boxItem = tk.Label(self.label, image=box.imageSm)
                boxItem.image = box.imageSm
                boxItem.grid(column=0, columnspan=2,
                             row=currentRow, rowspan=4)
                self.cartItems.append(boxItem)

                # Set Product Name
                name = tk.Label(self.label, text=box.name,
                                font="Helvetica 15 bold")
                name.grid(row=currentRow, column=2, columnspan=3, sticky="w")
                self.cartItems.append(name)

                # Set Product price
                price = tk.Label(self.label, text="Price: $"+"{:.2f}".format(box.price)+"/ea",
                                 font="Helvetica 15")
                price.grid(row=currentRow+1, column=2,
                           columnspan=3, sticky="w")
                self.cartItems.append(price)

                # show addons
                addons = tk.Label(self.label, text=self.getAddOns(
                    box))
                addons.grid(column=2, row=currentRow +
                            2, columnspan=5, sticky="w")
                self.cartItems.append(addons)

                # show quantity of boxes
                quant = tk.Label(self.label, text="Quantity: " + str(box.quantity)
                                 )
                quant.grid(column=9, row=currentRow, sticky="e")
                total += self.getBoxTotal(box)
                self.cartItems.append(quant)

                # Remove item button
                removeBtn = tk.Button(
                    self.label, text='Remove', command=lambda: self.removeItemFromCart(box))
                removeBtn.grid(row=currentRow+1, column=9, sticky="e")
                self.cartItems.append(removeBtn)

                # seperator
                sep = ttk.Separator(self.label)
                sep.grid(row=currentRow+4, column=0,
                         columnspan=10, sticky="ew")
                self.cartItems.append(sep)
                currentRow += 5

            # display total
            totalLab = tk.Label(self.label, text="Total: $" +
                                "{:.2f}".format(total))
            totalLab.grid(column=9, row=currentRow, sticky="e")
            self.cartItems.append(totalLab)

            # checkout button
            checkoutBtn = tk.Button(
                self.label, text='Checkout', font="Helvetica 18", command=self.ViewCheckoutPageNav)
            checkoutBtn.grid(row=currentRow+1, column=9, sticky="e")
            self.cartItems.append(checkoutBtn)
        else:
            # display empty cart message
            tk.Label(self.label, text='Your cart is empty!', font="Helvetica 25 bold").grid(
                row=3, column=2, columnspan=8, pady=(30, 0))
            tk.Button(self.label, text='Back to Store', width=15,
                      command=self.hide).grid(row=4, column=5, columnspan=2)

    def removeItemFromCart(self, box):
        for item in self.cart:
            if(item.name == box.name and item.addOns == box.addOns):
                self.cart.remove(box)

        # reinit cart
        for item in self.cartItems:
            item.grid_forget()
        self.cartItems.clear()
        self.setCart()

    def addItemToCart(self, newBox):
        found = False
        if(len(self.cart) == 0):
            self.cart.append(newBox)
        else:
            for box in self.cart:
                if(box.name == newBox.name and box.addOns == newBox.addOns):
                    box.quantity += newBox.quantity
                    found = True
            if(found == False):
                self.cart.append(newBox)

    def clearCart(self):
        # remove all cart related items
        # possible improvement of placing items in a frame and just forgetting the whole frame
        for item in self.cartItems:
            item.grid_forget()
        self.cartItems.clear()
        self.cart.clear()

        # reset cart
        self.setCart()

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
