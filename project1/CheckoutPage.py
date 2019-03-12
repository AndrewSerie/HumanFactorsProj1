import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from page import Page
from field import Field
from ViewCartPage import ViewCartPage
import os
from pathlib import Path    # Handing cross-platform paths


class CheckoutPage(Page):
    def __init__(self, master=None, *args, **kwargs):
        # configure page
        Page.__init__(self, *args, **kwargs)
        self.cart = ViewCartPage()

        # Set breadcrumb frame
        self.label = tk.LabelFrame(
            self, text="Store > Cart > Checkout", padx=10, pady=10)
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
        tk.Button(self.label, text='Back to Cart', width=15,
                  command=self.ViewCartPageNav).grid(row=0, column=0, columnspan=2, sticky="nw")
        tk.Button(self.label, text='Store', width=15,
                  command=self.hide).grid(row=0, column=10, columnspan=2, sticky="ne")

        # Set Main Image
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        imgPath = imagesPath / "bluebox.png"
        img = tk.PhotoImage(file=rf"{imgPath}")
        mainImage = tk.Label(self.label, image=img)
        mainImage.image = img
        mainImage.grid(row=0, column=2, columnspan=8)

        self.fields = [
            Field("Full Name", True),
            Field("Address", True),
            Field("Suite/Apt", False),
            Field("City", True),
            Field("State", True),
            Field("Zip Code", True),
            Field("Card Number", True),
            Field("Exp", True),
            Field("CVV2", True),
            Field("Billing Zip", True)
        ]

        # Add fields
        self.entries = []
        row = 1
        col = 1
        for field in self.fields:
            # set label
            labelText = field.name
            if(field.required):
                labelText += "*"
            lab = tk.Label(self.label, text=labelText,
                           font="Helvetica 14 bold")
            lab.grid(row=row, column=col, sticky="w")

            # set entry field
            entry = tk.Entry(self.label)
            entry.bind("<Button-1>", lambda event,
                       entry=entry: self.clearFieldOnClick(event, entry))
            entry.grid(row=row, column=col+1, columnspan=2)

            self.entries.append((field, entry, row))
            row += 1

            # Place card info image after zip (much better ways to go about this) -AS
            if(field.name == "Zip Code"):
                tk.Label(self.label, text="This store accepts Visa, Mastercard, AMEX, Discover and Optima cards.").grid(
                    row=row, column=col, columnspan=6, sticky="w")
                cwd = os.getcwd()
                imagesPath = Path(cwd, "images")
                imgPath = imagesPath / "cards.png"
                img = tk.PhotoImage(file=rf"{imgPath}")
                cards = tk.Label(self.label, image=img)
                cards.image = img
                cards.grid(row=row+1, column=col, columnspan=6, sticky="w")
                row += 2

        # Discounts
        if(self.getNumBoxes() >= 150):
            tk.Label(self.label, text="Your order has qualified for a 10% discount and free shipping!", fg="dark red").grid(
                row=12, column=6, columnspan=5, sticky="w")
        elif(self.getNumBoxes() >= 50):
            tk.Label(self.label, text="Your order has qualified for free shipping!", fg="dark red").grid(
                row=12, column=6, columnspan=5, sticky="w")
        else:
            tk.Label(self.label, text="Sorry, you do not qualify for any discounts.\nOrder at least 50 boxes for free shipping and 150 boxes for a 10% discount.", fg="dark red", wraplength=500, justify="left").grid(
                row=12, column=6, columnspan=5, sticky="w",)

        # Subtotal
        tk.Label(self.label, text="Sub total: ${:.2f}".format(
            self.getOrderTotal())).grid(row=13, column=6, columnspan=5, sticky="w")

        # shipping
        if(self.getNumBoxes() < 50):
            tk.Label(self.label, text="Shipping: ${:.2f}".format(
                self.getOrderTotal() * .05)).grid(row=14, column=6, columnspan=5, sticky="w")

        # 10% discount notify
        if(self.getNumBoxes() >= 150):
            tk.Label(self.label, text="Total: ${:.2f}".format(
                self.getOrderTotal() * .9)).grid(row=15, column=6, columnspan=5, sticky="w")
        elif(self.getNumBoxes() >= 50):
            tk.Label(self.label, text="Total: ${:.2f}".format(
                self.getOrderTotal())).grid(row=15, column=6, columnspan=5, sticky="w")
        else:
            tk.Label(self.label, text="Total: ${:.2f}".format(
                self.getOrderTotal()*1.05)).grid(row=15, column=6, columnspan=5, sticky="w")

        tk.Button(
            self.label, command=self.validate, text='Submit Order', font="Helvetica 18", width=15).grid(row=16, column=6, sticky="w")

    def clearFieldOnClick(self, event, e):
        e.delete(0, "end")

    def validate(self):
        error = False
        count = 0  # much better ways
        for entry in self.entries:
            if(not entry[1].get() and count != 2):
                self.errorMessage(entry[1])
                error = True
            count += 1
        if(not error):
            self.processOrder()

    def errorMessage(self, field):
        field.insert(0, "This field is required")

    def processOrder(self):
        tk.messagebox.showinfo(
            "Order Success", "Your order has been placed successfully!")
        self.navHome()

    def ViewCartPageNav(self):
        self.hide()
        self.master.ViewCartPageNav()

    def getNumBoxes(self):
        return self.cart.getNumBoxes()

    def getOrderTotal(self):
        total = 0.0
        for box in self.cart.cart:
            total += self.cart.getBoxTotal(box)
        return total

    def navHome(self):
        self.cart.cart.clear()
        self.hide()
