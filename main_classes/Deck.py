import random
from errors_and_tests import Error
from main_classes.Card import Card


class Deck:
    __deck_inst = None

    @staticmethod
    def get_instance():
        if Deck.__deck_inst is None:
            Deck()
        return Deck.__deck_inst

    def __init__(self):
        if Deck.__deck_inst is not None:
            raise Error.DeckError("second deck")
        else:
            self.__SIZE = 52
            self.__deck = []
            self.__generate_deck()
            Deck.__deck_inst = self

    def __generate_deck(self):
        for s in Card.suits:
            for v in Card.values:
                card = Card(v, s)
                self.__deck.append(card)

    def get_deck(self) -> list:
        return self.__deck
    
    def add_card(self, card: Card):
        if len(self.__deck) < self.__SIZE:
            self.__deck.insert(0, card)

    def draw_card(self) -> Card:
        if len(self.__deck) == 0:
            raise Error.DeckError("empty")
        try:
            return self.__deck.pop()
        except Exception:
            raise Error.DeckError

    def shuffle(self):
        if not self.__deck:
            raise ValueError
        else:
            available_cards = list(range(self.__SIZE))
            while len(available_cards) > 0:
                index_1 = random.choice(available_cards)
                available_cards.pop(available_cards.index(index_1))
                index_2 = random.choice(available_cards)
                available_cards.pop(available_cards.index(index_2))
                self.__deck[index_1], self.__deck[index_2] = self.__deck[index_2], self.__deck[index_1]

    def __str__(self):
        return str(self.__deck)
