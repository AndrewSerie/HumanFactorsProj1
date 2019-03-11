import tkinter as tk
from tkinter import ttk
from page import Page
from ViewCartPage import ViewCartPage
import os

class CheckoutPage(Page):
   def __init__(self, master = None, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.cart = ViewCartPage()
       self.label = tk.LabelFrame(self, text="This is the Checkout Page")
       self.label.pack(side="top", fill="both", expand=True)
       scriptDir = os.getcwd()
       img = tk.PhotoImage(file=rf"{scriptDir}\UIProj\bluebox.png")
       mainImage = tk.Label(self.label, image = img)
       mainImage.image = img
       mainImage.grid(row = 0, column = 3, rowspan = 6, columnspan = 2)
       Home = tk.Button(self.label, text = 'Back to Store', command=self.hide).grid(row=0, column = 0, sticky=(tk.N + tk.W))
       tk.Button(self.label, text = 'Cart', command= self.ViewCartPageNav).grid(row = 0, column = 5, sticky = "n")
       self.fields = ["Full Name","Address","City","State","Zip Code", "Card Number","EXP", "CVV2", "Billing Zip"]
       self.entries = []
       row = 7
       col = 1
       ##vcmd = self.register(self.validate)          
       for field in self.fields:
          lab = tk.Label(self.label, text=field, anchor='w')
          ##ent = tk.Entry(self.label,validate='key', validatecommand=(vcmd, '%P'))
          ent = tk.Entry(self.label)
          ent.bind("<Button-1>", lambda event, ent=ent: self.clearFieldOnClick(event,ent))
          lab.grid(row=row, column = col)
          ent.grid(row=row, column = col+1)
          self.entries.append((field, ent, row))
          row+=1

       if(self.getNumBoxes() >= 50):
           tk.Label(self.label, text="Your order has qualified for free shipping!").grid(row=16, column = 4)
       else:
           tk.Label(self.label, text="Shipping = {:.2f}".format(self.getOrderTotal() * .05)).grid(row=16, column = 4)
       if(self.getNumBoxes() >= 150):
           tk.Label(self.label, text="Your total is {:.2f}".format(self.getOrderTotal() * .9)).grid(row=17, column = 4)
       else:
           tk.Label(self.label, text="Your total is {:.2f}".format(self.getOrderTotal())).grid(row=17, column = 4)
       if(self.getNumBoxes() < 50):
           tk.Label(self.label, text="Sorry, you do not qualify for any discounts\n You must order at least 50 boxes for free shipping and 150 boxes for a 10% discount.").grid(row=18, column = 4)

       self.submit = tk.Button(self.label,command = self.validate, text='Submit', width=10).grid(row = 19, column = 4)

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
       field.insert(0,"Field Invalid!")
       ##self.submit.config(state = DISABLED)
   def processOrder(self):
       orderComplete = tk.Tk()
       orderComplete.wm_title("Order Success")
       tk.Label(orderComplete, text="Congratulations! Your order has been completed").pack()
       B1 = ttk.Button(orderComplete, text="Okay", command= lambda: self.navHome(orderComplete))
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
