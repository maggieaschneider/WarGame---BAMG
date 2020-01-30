from tkinter import *
from screen_prepare_for_war import Screen_prepare_for_war
from screen_war import Screen_war
from screen_welcome_ import Screen_welcome
from cards import CardList
# any other
class WarGame_Manager(object):
    def __init__(self):
        self.root = Tk()
        self.screen = None
        self.player = None
        self.computer = None
        self.current_screen = None
        self.card_list = CardList
    def start_screen(self):
        self.root.title("Welcome to WarGame!")
        self.current_screen = Screen_welcome(self.root, self.onclose_card_selector)

    def onclose_card_selector(self):
        ''' This method is called when the Screen_card_selector closes.
            selected_card should contain the index in the list of the cards selected by the user.
            The method manages the assignment of the player and computer objects and then starts the
            Prepare for war screen.
            '''
        # Destroys the card selection window
        self.current_screen.destroy()

        # Continue on - prepare for war screen!
        self.setup_prepare_for_war()

    def setup_prepare_for_war(self):
        ''' This method is called to create the Prepare for war screen. '''
        self.root.title("Choose Your Cards!")

        self.current_screen = Screen_prepare_for_war(self.root, self.player, self.computer, self.onclose_prepare_for_war)

    def onclose_prepare_for_war (self):
        '''
        This method is called when the user presses button on the Prepare for war screen.
        The method closes the Screen_prepare_for_war and creates the war screen.
        '''
        self.current_screen.destroy()

        self.setup_war()


    def setup_battle(self):
        ''' This method is called to create the war screen. '''
        self.root.title ("WAR")

        self.current_screen = Screen_war(self.root, self.computer, self.onclose_battle)

    def onclose_battle (self):
        ''' This method is called after the war is over.  This method causes the program to exit. '''
        self.root.destroy()

def main():
    war = WarGame_Manager()
    war.start_screen()
    war.root.mainloop()

main()
