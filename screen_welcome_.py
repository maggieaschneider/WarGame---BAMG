from tkinter import *

class Screen_welcome(Frame):
    def __init__(self, master, card_list, call_on_selected):
        super(Screen_welcome, self).__init__(master)

        # Save the list of cards
        self.cards_list = card_list

        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''This method creates all of the widgets for card selector page.  '''
        Label(self, text="War - A Card Game").grid(row=0, column=0)
        Label(self, text="Grant Lewison, Maggie Schneider, Brian Too, Abigail Oliver").grid(row=1, column=0)
        # image goes here
        # grid: row=2, column=0
        Label(self, text="Click Below To Begin!").grid(row=3, column=0)
        Button(self, text="Let's Play", command=self.continue_clicked).grid(row=4, column=0)


    def continue_clicked(self):
        ''' This method is called when the Next button is clicked.  '''
        self.call_on_selected