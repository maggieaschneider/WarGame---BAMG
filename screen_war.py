from tkinter import *
import random
from cards import Card, CardList
class Screen_war(Frame):
    def __init__(self, master, call_on_next, player1, player2):
        super(Screen_war, self).__init__(master)

        # Save references to the card objects
        # NOT DONE

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next
        self.player1 = player1
        self.player2 = player2
        self.deck = CardList("cards")
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        ''' This method creates all of the widgets for the battle page. '''
        Label(self, text="You", font = "COMIC 10"
              ).grid(row=1, column=0)

        image = PhotoImage(file='cardBack.png')
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=0, sticky=W)

        Label(self, text="Computer", font = "COMIC 10").grid(row=1, column=3)

        image = PhotoImage(file="cardBack.png")
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=3, sticky=E)

        next_button = Button(self, text="Click To Draw",
                             font = "Helvetica 20", fg = "black", bg = "red", command=self.continue_clicked)

        next_button.grid(row=3, column=0, columnspan=4, sticky = N)

        Label(self, text="").grid(row=4)

        Label(self, text = "Points-", font = "COMIC 14").grid(row = 5, columnspan = 4)

        Label(self, text="You:", font = "COMIC 7").grid(row=6, column = 0, sticky = W)

        Label(self, text="Computer:", font = "COMIC 7").grid(row=6, column=3, sticky=W)

    def continue_clicked(self):
        self.deck.shuffle()
        self.p1list = []
        self.p2list = []
        int = 0
        for c in self.deck.card_list:
            if int %2==0:
                self.p1list.append(c)
            elif int %2==1:
                self.p2list.append(c)
            self.deck.card_list.remove(c)
            int+=1
        self.round()

    def round(self):
        p1card = self.p1list[0]
        image = PhotoImage(file=('cardImages/' + p1card.image))
        p1 = Label(self, image=image)
        p1.photo = image
        p1.grid(row=2, column=1)

        p2card = self.p2list[0]
        image = PhotoImage(file=('cardImages/' + p2card.image))
        p2 = Label(self, image=image)
        p2.photo = image
        p2.grid(row=2, column=2)



    def tied_war(self):
        # Still needs to be worked on
        return 0

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked.  '''
        self.call_on_selected()