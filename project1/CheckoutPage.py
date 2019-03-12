import tkinter as tk
from tkinter import ttk
from page import Page
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

        self.fields = ["Full Name", "Address", "City", "State",
                       "Zip Code", "Card Number", "EXP", "CVV2", "Billing Zip"]
        self.entries = []
        row = 7
        col = 1
        ##vcmd = self.register(self.validate)
        for field in self.fields:
            lab = tk.Label(self.label, text=field, anchor='w')
            ##ent = tk.Entry(self.label,validate='key', validatecommand=(vcmd, '%P'))
            ent = tk.Entry(self.label)
            ent.bind("<Button-1>", lambda event,
                     ent=ent: self.clearFieldOnClick(event, ent))
            lab.grid(row=row, column=col)
            ent.grid(row=row, column=col+1)
            self.entries.append((field, ent, row))
            row += 1

        if(self.getNumBoxes() >= 50):
            tk.Label(self.label, text="Your order has qualified for free shipping!").grid(
                row=16, column=4)
        else:
            tk.Label(self.label, text="Shipping = {:.2f}".format(
                self.getOrderTotal() * .05)).grid(row=16, column=4)
        if(self.getNumBoxes() >= 150):
            tk.Label(self.label, text="Your total is {:.2f}".format(
                self.getOrderTotal() * .9)).grid(row=17, column=4)
        else:
            tk.Label(self.label, text="Your total is {:.2f}".format(
                self.getOrderTotal())).grid(row=17, column=4)
        if(self.getNumBoxes() < 50):
            tk.Label(self.label, text="Sorry, you do not qualify for any discounts\n You must order at least 50 boxes for free shipping and 150 boxes for a 10% discount.").grid(
                row=18, column=4)

        tk.Button(
            self.label, command=self.validate, text='Submit', width=10).grid(row=19, column=4)

    def clearFieldOnClick(self, event, e):
        e.delete(0, "end")
        ##self.submit.config(state = NORMAL)

    def validate(self):
        error = False
        for entry in self.entries:
            if(not entry[1].get()):
                self.errorMessage(entry[1])
                error = True
        if(not error):
            self.processOrder()

    def errorMessage(self, field):
        field.insert(0, "Field Invalid!")
        ##self.submit.config(state = DISABLED)

    def processOrder(self):
        orderComplete = tk.Tk()
        orderComplete.wm_title("Order Success")
        tk.Label(orderComplete,
                 text="Congratulations! Your order has been completed").pack()
        B1 = ttk.Button(orderComplete, text="Okay",
                        command=lambda: self.navHome(orderComplete))
        B1.pack()

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

    def navHome(self, orderCompleteWindow):
        orderCompleteWindow.destroy()
        self.cart.cart.clear()
        self.hide()
