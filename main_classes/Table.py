from main_classes.Deck import Deck
from main_classes.Player import Player


class Table:
    __table_inst = None

    @staticmethod
    def get_instance():
        if Table.__table_inst is None:
            Table()
        return Table.__table_inst

    def __init__(self):
        if Table.__table_inst is not None:
            raise Exception("Error:: multiple tables")
        else:
            self.__players = []
            self.__drop_players = []
            self.__deck = Deck.get_instance()
            self.__cards_on_table = []
            self.__tokens_on_table = 0
            Table.__table_inst = self

    def set_players(self, players: list):
        self.__players = players

    def set_cards_on_table(self, cards_on_table: list):
        self.__cards_on_table = cards_on_table

    def drop_player(self, player: Player):
        self.__players.remove(player)
        self.__drop_players.append(player)

    def remove_player(self, player: Player):
        self.__players.remove(player)

    def get_players(self) -> list:
        return self.__players

    def get_players_cards(self) -> dict:
        players_cards = {}
        for player in self.__players:
            if player.is_playing():
                players_cards[player] = player.get_hand()
        return players_cards

    def get_deck(self) -> Deck:
        return self.__deck

    def get_cards_on_table(self) -> list:
        return self.__cards_on_table

    def get_tokens_on_table(self) -> int:
        return self.__tokens_on_table

    def add_player(self, player: Player):
        self.__players.append(player)

    def add_cards_on_table(self, cards: list):
        self.__cards_on_table.append(cards)

    def add_tokens_on_table(self, tokens: int):
        self.__tokens_on_table += tokens

    def reset_players(self):
        self.__players += self.__drop_players
        for player in self.__players:
            player.set_all_in(False)

    def __str__(self):
        players = self.__players
        if len(players) > 0:
            players = " " + str(players).replace(",", "").replace("[", "").replace("]", "")
        else:
            players = ""
        cards_on_table = self.__cards_on_table
        if len(cards_on_table) > 0:
            cards_on_table = "   " + str(cards_on_table).replace(",", "  ").replace("[", "").replace("]", "")
        else:
            cards_on_table = ""
        return f"\n============\nTable:\n Players:\n{players} Cards on table:\n{cards_on_table}============\n"
