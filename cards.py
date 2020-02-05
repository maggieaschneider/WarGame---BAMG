import random
class Card (object):

    def __init__(self, name, value, image):
        self.name = name
        self.value = value
        self.image = image

    def __str__(self):
        pass


class CardList(object):
    def __init__(self, file_name):
        self.card_list = []
        text_file = open(file_name, "r")
        for line in text_file:
            line = line.strip()
            stats = line.split(",")
            card = Card(stats[0], stats[1], stats[2])
            self.card_list.append(card)

    def get_random_card(self, card_list):
        return random.choice(card_list)

    def return_list(self):
        return self.card_list