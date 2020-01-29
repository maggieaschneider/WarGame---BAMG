


class card (object):

    def __init__(self, image):
        self.image = image
        self.value = self.findValue()
        self.suit = self.findSuit()

    def findValue(self):
        # must include if statements for each royal card, J=11, etc.
        # rest of cards, find first
        return 0 # change this to become the value (int)

    def findSuit(self):
        # find the second letter of the name of the image and it will choose a class based on that
        # probably best to do if statemtents
        return 0 # change this to become the suit (str (letter))

    def war(self, enemy):
        pass

    def lost(self):
        ''' Prints a message. '''
        pass

    def __str__(self):
        ''' Prints the stuff '''
        pass


class CardList(object):
    def __init__(self, file_name):

        self.card_list = []

        text_file = open(file_name, "r")


