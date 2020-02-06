from tkinter import *
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

        Label(self, text="Computer", font = "COMIC 10"
              ).grid(row=1, column=3)

        image = PhotoImage(file="cardBack.png")
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=3, sticky=E)

        next_button = Button(self, text="Click To Draw",
                             font = "Helvetica 20", fg = "black", bg = "red", command=self.continue_clicked())

        next_button.grid(row=3, column=4, sticky = E)

        Label(self, text="").grid(row=4)

        Label(self, text = "Points-", font = "COMIC 15").grid(row = 5, columnspan = 4)

        Label(self, text="You:", font = "COMIC 7").grid(row=6, column = 0, sticky = W)

        Label(self, text="Computer:", font = "COMIC 7").grid(row=6, column=3, sticky=W)

    def war_clicked(self):
        ''' This method is called when the user presses the "WAR" button. '''
        image = PhotoImage(file=('cardImages' + self.p1list.get_random_card.name))
        p = Label(self, image=image)
        p.photo = image
        p.grid(row=2, column=1)

        image = PhotoImage(file=('cardImages' + self.p1list.get_random_card.name))
        p = Label(self, image=image)
        p.photo = image
        p.grid(row=2, column=2)

        ppoints = 0
        cpoints = 0

        if self.player1.card.value > self.player2.card.value:
            ppoints += 1
        elif self.player1.card.value < self.player2.card.value:
            cpoints += 1
        else:
            self.tied_war()
        if ppoints>=15 or cpoints>=15:
            self.exit_clicked()

    def continue_clicked(self):
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

    def tied_war(self):
        if self.player1.card.value == self.player2.card.value:
            return 0 # import a new random card
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked.  '''
        self.call_on_selected()