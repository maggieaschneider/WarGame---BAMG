from tkinter import *
from cards import CardList
import time
class Screen_war(Frame):
    def __init__(self, master, call_on_next, player1, player2):
        super(Screen_war, self).__init__(master)

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next
        self.player1 = player1
        self.player2 = player2
        self.deck = CardList("cards")
        self.create_widgets()
        self.grid()
        self.ppoints = 0
        self.cpoints = 0
        self.deck.shuffle()
        self.p1list = []
        self.p2list = []
        self.deck.shuffle()
        int = 0
        for c in self.deck.card_list:
            if int % 2 == 0:
                self.p1list.append(c)
            elif int % 2 == 1:
                self.p2list.append(c)
            self.deck.card_list.remove(c)
            int += 1

    def create_widgets(self):
        ''' This method creates all of the widgets for the battle page. '''
        Label(self, text="You", font = "COMIC 10").grid(row=1, column=0)
        Label(self, text="Your Card", font="COMIC 10").grid(row=1, column=1)

        image = PhotoImage(file='cardBack.png')
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=0, sticky=W)

        Label(self, text="Computer", font = "COMIC 10").grid(row=1, column=3)
        Label(self, text="Computer's Card", font="COMIC 10").grid(row=1, column=2)

        image = PhotoImage(file="cardBack.png")
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=3, sticky=E)

        self.next_button = Button(self, text="Click To Draw",
                             font = "Helvetica 20", fg = "black", bg = "red", command=self.round)

        self.next_button.grid(row=3, column=0, columnspan=4, sticky = N)

        Label(self, text="").grid(row=4)

        Label(self, text = "Points:", font = "COMIC 14").grid(row = 5, columnspan = 4)

        self.ppoint_label = Label(self, text="You:", font = "COMIC 15")
        self.ppoint_label.grid(row=6, column = 0, sticky = W)

        self.cpoint_label = Label(self, text="Computer:", font = "COMIC 15")
        self.cpoint_label.grid(row=6, column=3, sticky=W)

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
        if p1card.value==14 and p2card.value==2:
            self.cpoints += 1
            self.cpoint_label['text'] = "Computer:", self.cpoints
            self.p2list.remove(p2card)
            self.p2list.append(p2card)
            self.p1list.remove(p1card)
            self.p2list.append(p1card)
        elif p2card.value==14 and p1card==2:
            self.ppoints += 1
            self.ppoint_label['text'] = "You:", self.ppoints
            self.p1list.remove(p1card)
            self.p1list.append(p1card)
            self.p2list.remove(p2card)
            self.p1list.append(p2card)
        else:
            if p1card.value > p2card.value:
                self.ppoints += 1
                self.ppoint_label['text'] = "You:", self.ppoints
                self.p1list.remove(p1card)
                self.p1list.append(p1card)
                self.p2list.remove(p2card)
                self.p1list.append(p2card)
            elif p1card.value < p2card.value:
                self.cpoints += 1
                self.cpoint_label['text'] = "Computer:", self.cpoints
                self.p2list.remove(p2card)
                self.p2list.append(p2card)
                self.p1list.remove(p1card)
                self.p2list.append(p1card)
            else: # this is where we will do work on the tie screen
                # will require re-griding of p1 and p2 to fit new cards
                # have to figure out a way to show back card but make it have the value
                self.p1list.remove(p1card) # change all of these
                self.p1list.append(p1card) # ^
                self.p2list.remove(p2card) # ^
                self.p2list.append(p2card) # ^
                time.sleep(1)
        if self.ppoints >= 15:
            time.sleep(0.5) # ASK WANG HOW TO GET IT TO ONLY SLEEP ONE PART OF THE PROGRAM
            self.call_on_selected("p")
        if self.cpoints >= 15:
            time.sleep(0.5)
            self.call_on_selected("c")