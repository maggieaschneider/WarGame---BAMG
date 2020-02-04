class Card (object):

    def __init__(self, image_name):
        self.image = image_name
        self.value = self.findValue()

    def findValue(self):
        val = str(card.image_name)[0]
        if val == "J":
            val = 11
        elif val == "Q":
            val = 12
        elif val == "K":
            val = 12
        elif val == "A":
            val = 13
        return int(val)

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
        for line in text_file:
            line = line.strip()
            stats = line.split(",")
            card = Card(stats[0])
            self.card_list.append(card)