from tkinter import *


class Screen_prepare_for_war(Frame):
    def __init__(self, master, player1, player2, call_on_next):
        super(Screen_prepare_for_war, self).__init__(master)

        self.player1 = player1
        self.player2 = player2
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Label(self, text = "You", font = "COMIC 10"
              ).grid(row = 1, column = 0)

        image = PhotoImage(file="cardBack/" + self.image)
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=0, sticky=W)

        Label(self, text="Computer", font = "COMIC 10"
              ).grid(row=1, column=1)

        image = PhotoImage(file="cardBack/" + self.image)
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=1, sticky=W)

        next_button = Button(self, text = "Click to play!", font = "Helvetica 20", fg = "black", bg = "red", command = self.continue_clicked)
        next_button.grid(row = 3, columnspan = 2)

    def continue_clicked(self):
        self.call_on_selected()