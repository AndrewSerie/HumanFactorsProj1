# ********************************************************
# ***    Students: Mike Bauer                          ***
# ***              Adam Decker                         ***
# ***              Andrew Serie                        ***
# ***              Sean Walter                         ***
# ***       Class: Human Factors and User Interface    ***
# ***  Instructor: Gamradt                             ***
# ***  Assignment: 2                                   ***
# ***    Due Date: 02-12-19                            ***
# ********************************************************
# *** Description: This project allows customers to    ***
# ***              purchase boxes and box accessories  ***
# ***              with a simple to use UI designed    ***
# ***              using Python tk/ttk                 ***
# ********************************************************


import tkinter as tk
from tkinter import ttk
import os
from pathlib import Path    # Handing cross-platform paths
from box import Box
from ViewCartPage import ViewCartPage
from ViewItemPage import ViewItemPage
from CheckoutPage import CheckoutPage


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

        boxes = [Box("8\" Square Box", 0.51, squareBox, squareBoxSm, "Small 8in. corrugated box that can be used for many applications including, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("11\" Square Box", 1.22, squareBox, squareBoxSm,
                     "Medium 11in. corrugated box that can be used for many applications including, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("14\" Square Box", 1.33, squareBox, squareBoxSm,
                     "Large 14in. corrugated box that can be used for many applications including, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("16\" Square Box", 1.67, squareBox, squareBoxSm,
                     "Large 16in. corrugated box that can be used for many applications including, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("12\"x9\"x6\" Rectangle Box", 0.80, rectangleBox, rectangleBoxSm,
                     "Small rectangular corrugated box that can be used for many applications including, but not limited to: shipping, moving, and storage. Now environment friendly!"),
                 Box("13\"x9\"x11\" Rectangle Box", 1.24, rectangleBox, rectangleBoxSm,
                     "Medium rectangular corrugated box that can be used for many applications including, but not limited to: shipping, moving, and storage. Now environment friendly!"),
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


def about(event):
    aboutUs()


def aboutUs():
    aboutUsWindow = tk.Tk()
    aboutUsWindow.wm_title("About")

    aboutUsWindow.grid_columnconfigure(0, weight=1)
    aboutUsWindow.grid_columnconfigure(1, weight=1)
    aboutUsWindow.grid_columnconfigure(2, weight=1)
    aboutUsWindow.wm_geometry("400x275")

    tk.Label(aboutUsWindow, text="About Us",
             font="Helvetica 16 bold").grid(row=0, column=0, columnspan=3, sticky="w")
    tk.Label(aboutUsWindow, text="We are a small company founded by 4 people who have always had a passion for corrugated fiberboard, or as its commonly known, cardboard.  We started creating our own boxes of all sizes and giving them away for free. Soon we realized that we could turn our passion into a business and the rest is history!",
             wraplength=400, justify="left").grid(row=1, column=0, columnspan=3, sticky="w")
    tk.Label(aboutUsWindow, text="Authors",
             font="Helvetica 16 bold").grid(row=2, column=0, sticky="w")
    tk.Label(aboutUsWindow, text="Mike Bauer\n Adam Decker\n Andrew Serie\nSean Walter").grid(
        row=3, column=0, rowspan=4, sticky="w")
    tk.Label(aboutUsWindow, text="Assignment",
             font="Helvetica 16 bold").grid(row=2, column=1, sticky="w")
    tk.Label(aboutUsWindow, text="1 & 2 - tk/ttk").grid(
        row=3, column=1, sticky="w")
    tk.Label(aboutUsWindow, text="Course",
             font="Helvetica 16 bold").grid(row=2, column=2, sticky="w")
    tk.Label(aboutUsWindow, text="SE330 Human Factors").grid(
        row=3, column=2, sticky="w")
    ttk.Button(aboutUsWindow, text="Close",
               command=lambda: aboutUsWindow.destroy()).grid(row=7, column=0, columnspan=3)


def contact(event):
    contactUs()


def contactUs():
    contactUsWindow = tk.Tk()
    contactUsWindow.wm_title("Contact")
    contactUsWindow.wm_geometry("300x150")

    contactUsWindow.grid_columnconfigure(0, weight=1)
    contactUsWindow.grid_columnconfigure(1, weight=1)
    contactUsWindow.grid_columnconfigure(2, weight=1)

    tk.Label(contactUsWindow, text="Customer Support",
             font="Helvetica 16 bold").pack()
    tk.Label(contactUsWindow, text="help@bluebox.com").pack()
    tk.Label(contactUsWindow, text="+1 605-123-4567").pack()
    tk.Label(contactUsWindow, text="Toll Free - 24/7 Support").pack()
    ttk.Button(contactUsWindow, text="Close",
               command=lambda: contactUsWindow.destroy()).pack()


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
    helpMenu.add_command(label='About', underline=1,
                         command=aboutUs, accelerator="Command+A")
    helpMenu.add_command(label='Contact', underline=0,
                         command=contactUs, accelerator="Command+C")
    menuBar.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=menuBar)
    root.bind_all("<Command-a>", about)
    root.bind_all("<Command-c>", contact)

    # main loop
    root.mainloop()
