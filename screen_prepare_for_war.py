from tkinter import *


class Screen_prepare_for_war(Frame):
    def __init__(self, master, call_on_next):
        super(Screen_prepare_for_war, self).__init__(master)

        # NOT DONE

        #  return control after the player hits "Next"
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        # NOT DONE


    def continue_clicked(self):
        ''' This method is called when the Next button is clicked.  '''
        self.call_on_selected(self.card.get())