from tkinter import *


class Screen_war(Frame):
    def __init__(self, master, call_on_next):
        super(Screen_war, self).__init__(master)

        # Save references to the card objects
        # NOT DONE

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        ''' This method creates all of the widgets for the battle page. '''
        # NOT DONE

    def war_clicked(self):
        ''' This method is called when the user presses the "WAR" button. '''
        # NOT DONE

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked.  '''
        self.call_on_selected()