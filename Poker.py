from main_classes.Player import Player
from main_classes.Table import Table
from main_classes.Combination import Combination


class Poker:
    __poker_inst = None

    @staticmethod
    def get_instance():
        if Poker.__poker_inst is None:
            Poker()
        return Poker.__poker_inst

    def __init__(self):
        if Poker.__poker_inst is not None:
            raise Exception("Error:: multiple poker games")
        else:
            self.__table = Table.get_instance()
            self.__combination = Combination.get_instance()
            self.__min_bid = 0
            Poker.__poker_inst = self

    def get_table(self) -> Table:
        return self.__table

    def get_combination(self) -> Combination:
        return self.__combination

    def add_player(self, player=None, name="", player_id=0, tokens=0):
        if player is None:
            player = Player(name, player_id, tokens)
        if isinstance(player, Player):
            self.__table.add_player(player)
        else:
            raise Exception("Error:: expecting a variable of type Player")

    def add_players(self, players: list):
        for player in players:
            if not isinstance(player, Player):
                raise Exception("Error:: expecting a variable of type Player")
        self.__table.set_players(players)

    def __same_total_bid(self) -> bool:
        total_bid = self.__table.get_players()[0].get_total_bid()
        print(self.__table.get_players())
        for player in self.__table.get_players():
            print(player.__str__(False), player.get_total_bid(), total_bid)
            if player.get_total_bid() != total_bid:
                return False
        return True

    def __player_action(self, player: Player, round_min_bid: int) -> int:
        if player.get_all_in():
            return round_min_bid
        while True:
            bid = input(f"{player.__str__(False)} enter bid amount or 'drop', 'pass', 'call' or 'all in': ")
            if bid == "pass":
                if player.p_pass(self.__same_total_bid()):
                    break
                else:
                    print(f"{player.__str__(False)} cannot pass.")
            elif bid == "drop":
                self.__table.drop_player(player)
                player.drop()
                break
            elif bid == "call":
                print(round_min_bid, player.get_total_bid())
                round_min_bid = max(round_min_bid, self.__min_bid*2)
                bid = abs(round_min_bid - player.get_total_bid())
                self.__table.add_tokens_on_table(bid)
                player.bid(bid)
                break
            elif bid == "all in":
                bid = player.get_tokens()
                self.__table.add_tokens_on_table(bid)
                round_min_bid = bid
                player.bid(bid)
                player.set_all_in(True)
                print(player.__str__(False), player.get_all_in())
                break
            else:
                try:
                    bid = int(bid)
                    if bid >= max(round_min_bid, self.__min_bid*2):
                        if player.bid(bid):
                            self.__table.add_tokens_on_table(bid)
                            # if round_min_bid != self.__min_bid*2:
                            round_min_bid += bid
                            # else:
                            #     round_min_bid = bid
                            print(round_min_bid)
                            break
                    else:
                        print(f"The minimum bid is {round_min_bid}.")
                except ValueError:
                    print("Invalid input try again.")
        return round_min_bid

    def __start_bidding(self, first_round: bool):
        round_min_bid = 0
        players = self.__table.get_players()
        i = 0
        turn_count = 0
        total_players = len(players)
        while i < len(players):
            if i < 2 and first_round:
                players[i].bid(self.__min_bid * (i + 1))
                self.__table.add_tokens_on_table(self.__min_bid * (i + 1))
                if i == 1:
                    first_round = False
            else:
                round_min_bid = self.__player_action(players[i], round_min_bid)
                turn_count += 1
            if self.__same_total_bid() and turn_count >= len(players):
                break
            elif total_players > len(players):
                total_players -= 1
                if len(players) == 1:
                    break
                if i >= len(players):
                    i = 0
            else:
                # print("A")
                i = (i + 1) % len(players)

        for player in self.__table.get_players():
            player.reset_total_bid()

    def game_setup(self, min_bid):
        self.__min_bid = min_bid
        if len(self.__table.get_players()) > 2:
            self.__table.get_deck().shuffle()
            for player in self.__table.get_players():
                player.draw()
            self.__table.set_cards_on_table([self.__table.get_deck().draw_card() for _ in range(3)])

            self.__start_bidding(True)

        else:
            raise Exception("Error:: there are not enough players")

    def round(self):
        if len(self.__table.get_players()) > 1:
            self.__table.add_cards_on_table(self.__table.get_deck().draw_card())

            self.__start_bidding(False)

        else:
            return

    def end_round(self) -> bool:
        combination_numbers = None
        if len(self.__table.get_players()) > 1:
            self.__combination.set_players_cards(self.__table.get_players_cards())
            self.__combination.set_cards_on_table(self.__table.get_cards_on_table())
            self.__combination.compute_combinations()
            combination_numbers = {player: player.get_cards_combination_number() for player in self.__table.get_players()}
            combination_numbers = list({k: v for k, v in sorted(combination_numbers.items(), key=lambda item: item[1])}.items())
            combination_numbers[0][0].set_tokens(combination_numbers[0][0].get_tokens() + self.__table.get_tokens_on_table())
            print(f"Scores: \n Winner: {combination_numbers[0][0].__str__(False)}")
            for player_number in combination_numbers:
                print(f"{player_number[0]}")
        elif len(self.__table.get_players()) == 1:
            player = self.__table.get_players()[0]
            player.set_tokens(player.get_tokens() + self.__table.get_tokens_on_table())
            print(f"Winner: {self.__table.get_players()[0].__str__(False)}")
        else:
            raise Exception("Error:: there are no players")

        for player in self.__table.get_players():
            if player.get_tokens() < 1:
                self.__table.get_players().remove(player)
        if self.__table.get_players() == 1:
            print(f"Game finished: Winner {combination_numbers[0]}")
            self.__table.reset_players()
            return True
        self.__table.reset_players()
        return False

# boris = Player("Boris", 0, 12)
# alice = Player("Alice", 1, 15)
# felix = Player("Felix", 2, 13)
#
# table.set_players([boris, alice, felix])
# print(table)
# # print(deck)
# # print("=====================")
# deck.shuffle()
#
# for i in table.get_players():
#     i.draw()
#
# table.set_cards_on_table([deck.draw_card() for i in range(3)])
# print(table)
# # print(deck)
# # print(len(deck.get_deck()))
#
# for i in table.get_players():
#     bid = int(input("{} please to enter amount of tokens to bid: ".format(i.get_name())))
#     i.bid(bid)
#     table.add_tokens_on_table(bid)
#
# print("Tokens on table: {}".format(table.get_tokens_on_table()))
#
# table.add_cards_on_table(deck.draw_card())
#
# for i in table.get_players():
#     bid = int(input("{} please to enter amount of tokens to bid: ".format(i.get_name())))
#     i.bid(bid)
#     table.add_tokens_on_table(bid)
#
# print("Tokens on table: {}".format(table.get_tokens_on_table()))
#
# table.add_cards_on_table(deck.draw_card())
#
# for i in table.get_players():
#     bid = int(input("{} please to enter amount of tokens to bid: ".format(i.get_name())))
#     i.bid(bid)
#     table.add_tokens_on_table(bid)
#
# print("Tokens on table: {}".format(table.get_tokens_on_table()))
#
# print(table)
# combination.set_cards_on_table(table.get_cards_on_table())
# combination.set_players_cards(table.get_players_cards())
# combination.set_cards_on_table(table.get_cards_on_table())
# combination.compute_combinations()
# for player in table.get_players():
#     print(combination.get_player_combination_number(player))
