from tkinter import *

import random as btn


class Main(Frame):
    def __init__(self, batya):
        super(Main, self).__init__(batya)
        self.startUI()

    def startUI(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+200+200")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()


btn = Button(root, text="Камень", font=("Times New Roman", 15))
btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15))
btn3 = Button(root, text="Бумага", font=("Times New Roman", 15))

btn.place(x=10, y=100, width=120, height=50)
btn2.place(x=155, y=100, width=120, height=50)
btn3.place(x=300, y=100, width=120, height=50)
