


class card (object):

    def __init__(self, image):

        self.image = image

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


