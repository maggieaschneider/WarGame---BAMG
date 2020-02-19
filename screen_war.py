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

        Label(self, text="Computer", font = "COMIC 10").grid(row=1, column=3)
        Label(self, text="Computer's Card", font="COMIC 10").grid(row=1, column=2)

        self.next_button = Button(self, text="Click To Draw",
                             font = "Helvetica 20", fg = "black", bg = "red", command=self.round)

        self.next_button.grid(row=3, column=4, columnspan=4, sticky = N)

        self.pLabel = Label(self, text = "Points:", font = "COMIC 14")
        self.pLabel.grid(row = 0, column=4)

        self.ppoint_label = Label(self, text="You:", font = "COMIC 15")
        self.ppoint_label.grid(row=1, column = 4, sticky=S)

        self.cpoint_label = Label(self, text="Computer:", font = "COMIC 15")
        self.cpoint_label.grid(row=2, column=4)

    def round(self):
        image = PhotoImage(file='cardBack.png')
        self.back1 = Label(self, image=image)
        self.back1.photo = image
        self.back1.grid(row=2, column=0, sticky=W)

        image = PhotoImage(file="cardBack.png")
        self.back2 = Label(self, image=image)
        self.back2.photo = image
        self.back2.grid(row=2, column=3, sticky=E)

        self.p1card = self.p1list[0]
        image = PhotoImage(file=('cardImages/' + self.p1card.image))
        p1 = Label(self, image=image)
        p1.photo = image
        p1.grid(row=2, column=1)

        self.p2card = self.p2list[0]
        image = PhotoImage(file=('cardImages/' + self.p2card.image))
        p2 = Label(self, image=image)
        p2.photo = image
        p2.grid(row=2, column=2)
        if self.p1card.value==14 and self.p2card.value==2:
            self.cpoints += 1
            self.cpoint_label['text'] = "Computer:", self.cpoints
            self.p2list.remove(self.p2card)
            self.p2list.append(self.p2card)
            self.p1list.remove(self.p1card)
            self.p2list.append(self.p1card)
        elif self.p2card.value==14 and self.p1card==2:
            self.ppoints += 1
            self.ppoint_label['text'] = "You:", self.ppoints
            self.p1list.remove(self.p1card)
            self.p1list.append(self.p1card)
            self.p2list.remove(self.p2card)
            self.p1list.append(self.p2card)
        else:
            if self.p1card.value > self.p2card.value:
                self.ppoints += 1
                self.ppoint_label['text'] = "You:", self.ppoints
                self.p1list.remove(self.p1card)
                self.p1list.append(self.p1card)
                self.p2list.remove(self.p2card)
                self.p1list.append(self.p2card)
            elif self.p1card.value < self.p2card.value:
                self.cpoints += 1
                self.cpoint_label['text'] = "Computer:", self.cpoints
                self.p2list.remove(self.p2card)
                self.p2list.append(self.p2card)
                self.p1list.remove(self.p1card)
                self.p2list.append(self.p1card)
            else:
                self.master.update()
                time.sleep(2)
                self.tie()
                self.master.update()
                time.sleep(1.5)
                self.p1.destroy()
                self.p2.destroy()
                self.p3.destroy()
                self.p4.destroy()
                self.p5.destroy()
                self.p6.destroy()
                self.p7.destroy()
                self.p8.destroy()
        if self.ppoints >= 12:
            self.master.update()
            time.sleep(1.25)
            self.call_on_selected("p")
        if self.cpoints >= 12:
            self.master.update()
            time.sleep(1.25)
            self.call_on_selected("c")
    def tie(self):

            self.back1.destroy()
            self.back2.destroy()

            p1c1 = self.p1list[0]
            self.p1list.remove(p1c1)
            image = PhotoImage(file=('cardBack.png'))
            self.p1 = Label(self, image=image)
            self.p1.photo = image
            self.p1.grid(row=2, column=0)

            p1c2 = self.p1list[1]
            self.p1list.remove(p1c2)
            image = PhotoImage(file=('cardBack.png'))
            self.p2 = Label(self, image=image)
            self.p2.photo = image
            self.p2.grid(row=2, column=1)

            p1c3 = self.p1list[2]
            self.p1list.remove(p1c3)
            image = PhotoImage(file=('cardBack.png'))
            self.p3 = Label(self, image=image)
            self.p3.photo = image
            self.p3.grid(row=2, column=2)

            p2c1 = self.p2list[0]
            self.p2list.remove(p2c1)
            image = PhotoImage(file=('cardBack.png'))
            self.p4 = Label(self, image=image)
            self.p4.photo = image
            self.p4.grid(row=3, column=0)

            p2c2 = self.p2list[1]
            self.p2list.remove(p2c2)
            image = PhotoImage(file=('cardBack.png'))
            self.p5 = Label(self, image=image)
            self.p5.photo = image
            self.p5.grid(row=3, column=1)

            p2c3 = self.p2list[2]
            self.p2list.remove(p2c3)
            image = PhotoImage(file=('cardBack.png'))
            self.p6 = Label(self, image=image)
            self.p6.photo = image
            self.p6.grid(row=3, column=2)

            p1cM = self.p1list[3]
            self.p1list.remove(p1cM)
            image = PhotoImage(file=('cardImages/' + p1cM.image))
            self.p7 = Label(self, image=image)
            self.p7.photo = image
            self.p7.grid(row=2, column=3)

            p2cM = self.p2list[3]
            self.p2list.remove(p2cM)
            image = PhotoImage(file=('cardImages/' + p2cM.image))
            self.p8 = Label(self, image=image)
            self.p8.photo = image
            self.p8.grid(row=3, column=3)

            if p1cM.value > p2cM.value:
                self.ppoints += 4
                self.master.update()
                time.sleep(0.5)
                self.ppoint_label['text'] = "You:", self.ppoints
                self.p1list.append(p1c1)
                self.p1list.append(p1c2)
                self.p1list.append(p1c3)
                self.p1list.append(p1cM)
                self.p1list.append(p2c1)
                self.p1list.append(p2c2)
                self.p1list.append(p2c3)
                self.p1list.append(p2cM)
            elif p1cM.value < p2cM.value:
                self.cpoints += 4
                self.master.update()
                time.sleep(0.5)
                self.cpoint_label['text'] = "Computer:", self.cpoints
                self.p2list.append(p1c1)
                self.p2list.append(p1c2)
                self.p2list.append(p1c3)
                self.p2list.append(p1cM)
                self.p2list.append(p2c1)
                self.p2list.append(p2c2)
                self.p2list.append(p2c3)
                self.p2list.append(p2cM)
            else:
                self.tie()