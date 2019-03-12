import tkinter as tk
from tkinter import ttk
from ViewCartPage import ViewCartPage
from page import Page
from box import Box
from addOnItem import AddOnItem
import os
class ViewItemPage(Page):
   addOns = [AddOnItem("Packing Tape",4.50),
             AddOnItem("Packing Wrap",15.00),
             AddOnItem("Packing Bags",10.00),
             AddOnItem("Shipping Labels",9.00),
             AddOnItem("Bubble Wrap",25.00),
             AddOnItem("Packing Peanuts",35.00)
             ]

   def __init__(self,master = None, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       scriptDir = os.getcwd()
       self.cart  =  ViewCartPage()
       self.label = tk.LabelFrame(self,text="This is the View Item Page")
       self.label.pack(side="top", fill="both", expand=True)
       img = tk.PhotoImage(file=rf"{scriptDir}\UIProj\bluebox.png")
       mainImage = tk.Label(self.label, image = img)
       mainImage.image = img
       mainImage.grid(row = 0, column = 2, padx = 100, rowspan = 6, columnspan = 2)
       tk.Button(self.label, text = 'Cart', command= self.ViewCartPageNav).grid(row = 0, column = 4, sticky = "n")
       Home = tk.Button(self.label, text = 'Back to Store', command=self.hide).grid(row=0, column = 0, sticky=(tk.N + tk.W))
    
   def sendBox(self,box):
       self.box = Box(box.description, box.price, box.image)
       boxItem = tk.Label(self.label,image = box.image)
       boxItem.image = box.image
       boxItem.grid(row = 6, column = 1, rowspan = 5)
       boxDescription = tk.Label(self.label, text = box.description).grid(row = 6, column = 2)
       boxPrice = tk.Label(self.label, text = "$" + str(box.price) + "/ea").grid(row = 7, column = 2)

       inStock = tk.Label(self.label, text = "IN STOCK").grid(row = 8, column = 2)
       self.boxQ = tk.IntVar()
       self.boxQ.set(box.quantity)
       self.boxQ.trace_add("write", self.updateQuantity)
       self.spinBox = tk.Spinbox(self.label, from_=1, to=2500,textvariable=self.boxQ)
       self.spinBox.grid(column = 4, row = 6)

       self.vars = []
       row = 7
       for pick in self.addOns: 
           var = tk.IntVar()
           chk = ttk.Checkbutton(self.label, text = pick.name +" $"+ str(pick.price), variable = var)
           chk.grid(row = row , column = 4)
           row+=1
           self.vars.append(var)
       AddToCartButton = tk.Button(self.label, text = "Add Item to Cart", command = self.addToCart).grid(row = row+1, column = 4)

   def clearBox(self):
        self.box = None

   def updateQuantity(self, *args):
       print("quantity updated") ## idk just need something here

   def addToCart(self):
       count = 0
       for var in self.vars:
           if(var.get() == 1):
               self.box.addOns.append(self.addOns[count])
               count += 1
       self.box.quantity = self.boxQ.get()
       self.cart.addItemToCart(self.box)
       self.hide()

   def ViewCartPageNav(self):
       self.hide()
       self.master.ViewCartPageNav()
