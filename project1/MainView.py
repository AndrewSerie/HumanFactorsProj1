import tkinter as tk
from tkinter import ttk
import os
from pathlib import Path    # Handing cross-platform paths
# Pages
from box import Box
from ViewCartPage import ViewCartPage
from ViewItemPage import ViewItemPage
from CheckoutPage import CheckoutPage

# Class for MainView


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # configure grid weights (resize)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)
        self.grid_columnconfigure(8, weight=1)
        self.grid_columnconfigure(9, weight=1)
        self.grid_columnconfigure(10, weight=1)
        self.grid_columnconfigure(11, weight=1)

        # Set nav button
        tk.Button(self, text='Cart', width=15,
                  command=self.ViewCartPageNav).grid(row=0, column=10, columnspan=2, sticky="ne", padx=10, pady=10)

        # Set Main Image
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        imgPath = imagesPath / "bluebox.png"
        img = tk.PhotoImage(file=rf"{imgPath}")
        mainImage = tk.Label(self, image=img)
        mainImage.image = img
        mainImage.grid(row=0, column=2, columnspan=8)

        # Set box Images
        cwd = os.getcwd()
        imagesPath = Path(cwd, "images")
        squareBoxPath = imagesPath / "box1.png"
        rectangleBoxPath = imagesPath / "box2.png"
        rectangleBoxSmPath = imagesPath / "box2_sm.png"
        squareBoxSmPath = imagesPath / "box1_sm.png"
        squareBox = tk.PhotoImage(file=rf"{squareBoxPath}")
        squareBoxSm = tk.PhotoImage(file=rf"{squareBoxSmPath}")
        rectangleBox = tk.PhotoImage(file=rf"{rectangleBoxPath}")
        rectangleBoxSm = tk.PhotoImage(file=rf"{rectangleBoxSmPath}")

        boxes = [Box("8\" Square Box", 0.51, squareBox, squareBoxSm, "Small 8in. corrugated box that can be used for many applications icluding, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("11\" Square Box", 1.22, squareBox, squareBoxSm,
                     "Medium 11in. corrugated box that can be used for many applications icluding, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("14\" Square Box", 1.33, squareBox, squareBoxSm,
                     "Large 14in. corrugated box that can be used for many applications icluding, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("16\" Square Box", 1.67, squareBox, squareBoxSm,
                     "Large 16in. corrugated box that can be used for many applications icluding, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("12\"x9\"x6\" Rectangle Box", 0.80, rectangleBox, rectangleBoxSm,
                     "Small rectangular corrugated box that can be used for many applications icluding, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("13\"x9\"x11\" Rectangle Box", 1.24, rectangleBox, rectangleBoxSm,
                     "Medium rectangular corrugated box that can be used for many applications icluding, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 ]

        currentRow = 1
        currentCol = 0
        for box in boxes:
            # set box image and button
            boxItem = tk.Label(self, image=box.image)
            boxItem.image = box.image
            boxItem.grid(row=currentRow, column=currentCol,
                         columnspan=3, rowspan=3)
            tk.Button(self, command=lambda box=box: self.ViewItemPageNav(
                box), text=box.name+"\n$"+"{:.2f}".format(box.price)+"/ea").grid(row=currentRow+3, column=currentCol, columnspan=3)

            # increment col and rows
            currentCol = currentCol+3
            if(currentCol > 10):
                currentCol = 0
                currentRow = currentRow+4

    def ViewItemPageNav(self, box):
        viewItemPageRef = ViewItemPage(self, self)
        viewItemPageRef.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        viewItemPageRef.clearBox()
        viewItemPageRef.sendBox(box)
        viewItemPageRef.show()

    def ViewCartPageNav(self):
        viewCartPageRef = ViewCartPage(self, self)
        viewCartPageRef.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        viewCartPageRef.show()

    def ViewCheckoutPageNav(self):
        viewCheckoutPageRef = CheckoutPage(self, self)
        viewCheckoutPageRef.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        viewCheckoutPageRef.show()


def aboutUs():
    aboutUsWindow = tk.Tk()
    aboutUsWindow.wm_title("About")
    aboutUsWindow.wm_geometry("385x250")
    aboutUsWindow.configure(background="white")
    tk.Label(aboutUsWindow, text="About us").pack()
    B1 = ttk.Button(aboutUsWindow, text="Close",
                    command=lambda: aboutUsWindow.destroy())
    B1.pack()


def contactUs():
    contactUsWindow = tk.Tk()
    contactUsWindow.wm_title("Contact Information")
    contactUsWindow.wm_geometry("385x250")
    contactUsWindow.configure(background="white")
    tk.Label(contactUsWindow, text="Contact us").pack()
    B1 = ttk.Button(contactUsWindow, text="Close",
                    command=lambda: contactUsWindow.destroy())
    B1.pack()


if __name__ == "__main__":
    # Window configure
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("BlueBox Store")
    root.wm_geometry("1280x720")
    root.configure(background="white")

    # Menu Bar  Help > About | Contact
    menuBar = tk.Menu(main)
    helpMenu = tk.Menu(menuBar, tearoff=0)
    helpMenu.add_command(label='About', underline=0, command=aboutUs)
    helpMenu.add_command(label='Contact', underline=0, command=contactUs)
    menuBar.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=menuBar)

    # main loop
    root.mainloop()
