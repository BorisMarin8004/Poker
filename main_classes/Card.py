from errors_and_tests import Error


class Card:
    suits = ("Clubs", "Diamonds", "Hearts", "Spades")
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, value="", suit=""):
        if isinstance(suit, str) and isinstance(value, str):
            # if suit in Deck.suits and value in Deck.values:
            self.__suit = suit
            self.__value = value
            # else:
            #     raise Error.CardError("suit|value not in Deck")
        else:
            raise Error.CardError("suit|value not str")

    def set_suit(self, suit: str):
        self.__suit = suit

    def set_value(self, value: str):
        self.__value = value

    def get_suit(self) -> str:
        return self.__suit

    def get_value(self) -> str:
        return self.__value

    def __str__(self):
        return f"({self.__value} | {self.__suit})\n"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, card):
        return isinstance(card, Card) and self.__suit == card.get_suit() and self.__value == card.get_value()


