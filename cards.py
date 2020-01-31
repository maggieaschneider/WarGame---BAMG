

class card (object):

    def __init__(self, image):
        self.image = image
        self.value = self.findValue()
        self.suit = self.findSuit()

    def findValue(self):
        val = str(card.image)[0]
        if val == "J":
            val = 11
        elif val == "Q":
            val = 12
        elif val == "K":
            val = 12
        elif val == "A":
            val = 13
        return int(val) # STILL NEEDS TO BE PUSHED

    def findSuit(self):
        suit = str(card.image)[1]
        # find the second letter of the name of the image and it will choose a class based on that
        # probably best to do if statements
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

