from errors_and_tests import Error
from main_classes.Deck import Deck


class Player:
    def __init__(self, name="", player_id=0, tokens=0):
        if isinstance(name, str) and isinstance(player_id, int) and isinstance(tokens, int):
            self.__name = name
            self.__id = player_id
            self.__hand = []
            self.__tokens = tokens
            self.__card_combination_number = 10
            self.__playing = True
            self.__total_bid = 0
            self.__all_in = False
        else:
            raise Error.PlayerError("name|player_id|tokens wrong type.")

    def set_name(self, name: str):
        self.__name = name

    def set_id(self, player_id: int):
        self.__id = player_id

    def set_tokens(self, tokens: int):
        self.__tokens = tokens

    def set_cards_combination_number(self, cards_combination_number: int):
        self.__card_combination_number = cards_combination_number

    def set_playing(self, playing: bool):
        self.__playing = playing

    def reset_total_bid(self):
        self.__total_bid = 0

    def set_all_in(self, all_in: bool):
        self.__all_in = all_in

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def get_hand(self) -> list:
        return self.__hand

    def get_tokens(self) -> int:
        return self.__tokens

    def get_cards_combination_number(self) -> int:
        return self.__card_combination_number

    def get_total_bid(self) -> int:
        return self.__total_bid

    def get_all_in(self) -> bool:
        return self.__all_in

    def draw(self):
        for i in range(2):
            self.__hand.append(Deck.get_instance().draw_card())

    def bid(self, tokens: int) -> bool:
        if self.__tokens - tokens > -1:
            if self.__tokens - tokens == 0:
                self.__all_in = True
            self.__tokens -= tokens
            self.__total_bid += tokens
            return True
        else:
            print(f"{self.__name} does not have that many tokens.")
            return False

    def drop(self):
        if self.__playing:
            for card in self.__hand:
                Deck.get_instance().add_card(card)
            self.__hand = []
            self.__playing = False
            self.__total_bid = 0
            self.__card_combination_number = 10
        else:
            raise Error.PlayerError("not playing")

    def is_playing(self) -> bool:
        return self.__playing

    def p_pass(self, same_total_bid: bool) -> bool:
        print(same_total_bid)
        if same_total_bid:
            self.bid(0)
            return True
        else:
            return False

    # def print_hand(self):
    #     if self.__hand:
    #         return f"{str(self.__hand[0])}, {self.__hand[1]}"
    #     else:
    #         return str(self.__hand)

    def __str__(self, b=True):
        if b:
            hand = self.__hand
            if len(hand) > 0:
                hand = str(hand).replace(",", "").replace("[", "").replace("]", "")
                hand = "     " + hand[:hand.index(")") + 2] + "     " + hand[hand.index(")") + 3:]
            else:
                hand = ""
            return f" Name: {self.__name}; id: {self.__id}; tokens: {self.__tokens};" \
                   f"\n    hand:\n{hand}" \
                   f"    cards combination number: {self.__card_combination_number}.\n"
        else:
            return f"{self.__name}, {self.__tokens} tokens\n"

    def __repr__(self):
        return self.__str__()
