class DeckError(Exception):
    def __init__(self, e=None):
        if e == "empty":
            self.message = "Error:: the deck is empty."
        elif e == "second deck":
            self.message = "Error:: multiple decks."
        else:
            self.message = "Unknown error with the deck object."

    def __str__(self):
        return self.message


class CardError(Exception):
    def __init__(self, e=None):
        if e == "suit|value not str":
            self.message = "Error:: suit and value have to be of a string type."
        elif e == "suit|value not in Deck":
            self.message = "Error:: suit or value are not from deck."
        else:
            self.message = "Error:: Unknown error with the card object."

    def __str__(self):
        return self.message


class PlayerError(Exception):
    def __init__(self, e=None):
        if e == "name|player_id|tokens wrong type.":
            self.message = "Error:: name, player_id or tokens are wrong data type."
        elif e == "not playing":
            self.message = "Error:: player is not playing."
        elif e == "no tokens":
            self.message = "The player does not have enough tokens."
        else:
            self.message = "Error:: Unknown error with the player object."

    def __str__(self):
        return self
#
# class TableError(Exception):
#     def __init__(self):
#
#     def __str__(self):
#         return self
#
# class PokerError(Exception):
#     def __init__(self):
#
#     def __str__(self):
#         return self
