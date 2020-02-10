from tkinter import *

class Screen_End(Frame):
    def __init__(self, master, call_on_next, winner):
        super(Screen_End, self).__init__(master)
        self.call_on_selected = call_on_next
        if winner=="p":
            self.winner="You"
        if winner=="c":
            self.winner="Computer"
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Label(self, text = "Thank you for playing!", fg = "Red").grid(row = 0, column = 0, sticky = N)
        Label(self, text = ("%s won the game! Congratulations to %s!" % (self.winner, self.winner.lower())),
              font="system 18").grid(row=1, column=0, sticky=N)
        image = PhotoImage(file="cardImages/back_cards-07.png")
        c = Label(self, image=image)
        c.photo = image
        c.grid(row=2, column=0)
        Button(self, text = "Click To Exit! Play again!", fg = "blue2", font="system 16", bg="cyan2",
               command=self.exit_clicked).grid(row = 3, column = 0, sticky = N)

    def exit_clicked(self):
        self.call_on_selected()