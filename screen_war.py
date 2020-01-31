from tkinter import *
import random

class Screen_war(Frame):
    def __init__(self, master, call_on_next, player1, player2):
        super(Screen_war, self).__init__(master)

        # Save references to the card objects
        # NOT DONE

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next
        self.player1 = player1
        self.player2 = player2
        self.create_widgets()
        self.grid()

    def get_random_card(self):

    def create_widgets(self):
        ''' This method creates all of the widgets for the battle page. '''
        Label(self, text="You"
              ).grid(row=1, column=0)

        image = PhotoImage(file="cards/" + self.get_random_card)
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=0, sticky=W)

        Label(self, text="Computer"
              ).grid(row=1, column=3)

        image = PhotoImage(file="cards/" + self.get_random_card)
        p = Label(self, image=image)
        p.photo = image

        p.grid(row=2, column=3, sticky=E)

        next_button = Button(self, text="Click to draw", command=self.continue_clicked)
        next_button.grid(row=3, column=4, sticky = E)

        Label(self, text= ""
              ).grid(row = 4)

        Label(self, text = "Points-"
              ).grid(row = 5, columnspan = 4)

        Label(self, text="You:"
              ).grid(row=6, column =0, sticky = W, command = self.war_clicked)

        Label(self, text="Computer:"
              ).grid(row=6, column=3, sticky=W, command=self.war_clicked)


    def war_clicked(self):
        ''' This method is called when the user presses the "WAR" button. '''
        ppoints = 0
        cpoints = 0
        if ppoints>=15 or cpoints>=15:
            self.exit_clicked()
        else:
            if self.player1.card.value > self.player2.card.value:
                ppoints += 1
            elif self.player1.card.value < self.player2.card.value:
                cpoints += 1
            else:
                self.tied_war()
    def tied_war(self):
        if self.player1.card.value == self.player2.card.value:
            # import a new random card

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked.  '''
        self.call_on_selected()