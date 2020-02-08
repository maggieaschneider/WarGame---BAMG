from tkinter import *


class Screen_End(Frame):
    def __init__(self, master, call_on_next):
        super(Screen_End, self).__init__(master)
        self.call_on_selected = call_on_next

    def create_widgets(self):
        Label(self, text = "Thank you for playing!", fg = "Red"
              ).grid(row = 0, column = 2, sticky = N)

        image = PhotoImage(file="cardImages/back_cards-07.png")
        c = Label(self, image=image)
        c.photo = image
        c.grid(row=1, column=0)

        Button(self, text = "Exit", fg = "Red"
               ).grid(row = 2, column = 4, sticky = E)

    def exit_clicked(self):
        self.call_on_selected()