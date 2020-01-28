from tkinter import *

class Screen_card_selector(Frame):
    def __init__(self, master, card_list, call_on_selected):
        super(Screen_card_selector, self).__init__(master)

        # Save the list of cards
        self.cards_list = card_list

        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''This method creates all of the widgets for card selector page.  '''
        # NOT DONE


    def continue_clicked(self):
        ''' This method is called when the Next button is clicked.  '''
        self.call_on_selected