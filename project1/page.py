import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.configure(background="white")
    def show(self):
        self.lift()
    def hide(self):
        self.destroy()
       

