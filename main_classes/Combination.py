from main_classes.Card import Card


def evaluate_combination_of_five_cards(card_combination: list) -> float:
    # print("Cards: ", card_combination)
    suits = [card.get_suit() for card in card_combination]
    values_index = [Card.values.index(card.get_value()) for card in card_combination]
    # print("Suits: ", suits)
    # print("Values index: ", values_index)
    set_size = 0
    dup = 0
    max_value_index = 0
    """Straight flush"""
    if len(set(suits)) == 1:
        if (max(values_index) - min(values_index)) == 4 and len(set(values_index)) == 5:
            return 1 - max(values_index) / 100
    """Four of a kind"""
    if len(set(values_index)) == 2:
        for i in range(len(values_index)):
            if values_index[i] == values_index[0]:
                set_size += 1
        if set_size == 1 or set_size == 4:
            if set_size == 4:
                max_value_index = max(values_index[:4]) / 100
            else:
                max_value_index = max(values_index[1:]) / 100
            return 2 - max_value_index
    """Full house"""
    if set_size == 3 or set_size == 2:
        return 3 - max(values_index) / 100
    """Flush"""
    if len(set(suits)) == 1:
        return 4 - max(values_index) / 100
    """Straight"""
    if (max(values_index) - min(values_index)) == 4 and len(set(values_index)) == 5:
        return 5 - max(values_index) / 100
    """Three of a kind"""
    if len(set(values_index)) == 3:
        for i in range(len(values_index)):
            for k in range(len(values_index)):
                if values_index[i] == values_index[k] and i != k:
                    dup += 1
                    if max_value_index < values_index[i] / 100:
                        max_value_index = values_index[i] / 100
        if dup == 3:
            return 6 - max_value_index
    """Two pair"""
    if dup == 4:
        return 7 - max_value_index
    """One pair"""
    if len(set(values_index)) == 4:
        for i in range(len(values_index)):
            for k in range(len(values_index)):
                if values_index[i] == values_index[k] and i != k:
                    if max_value_index < values_index[i] / 100:
                        max_value_index = values_index[i] / 100
        return 8 - max_value_index
    """High card"""
    return 9 - max(values_index) / 100


def get_card_combination_number(card_combination: list) -> float:
    possible_combinations_of_five_cards = []
    set_of_five = card_combination[:5]
    set_of_two = card_combination[5:]
    possible_combinations_of_five_cards.append(set_of_five.copy())

    """Each out of 2"""
    for i in range(len(set_of_two)):
        for k in range(len(set_of_five)):
            set_of_two[i], set_of_five[k] = set_of_five[k], set_of_two[i]
            possible_combinations_of_five_cards.append(set_of_five.copy())
            set_of_two[i], set_of_five[k] = set_of_five[k], set_of_two[i]

    """Both out of 2 (x, y) = set_of_two"""
    offset = 1
    for x_index in range(4):
        set_of_two[0], set_of_five[x_index] = set_of_five[x_index], set_of_two[0]
        for y_index in range(5-offset):
            set_of_two[1], set_of_five[y_index + offset] = set_of_five[y_index + offset], set_of_two[1]
            possible_combinations_of_five_cards.append(set_of_five.copy())
            set_of_two[1], set_of_five[y_index + offset] = set_of_five[y_index + offset], set_of_two[1]
        offset += 1
        set_of_two[0], set_of_five[x_index] = set_of_five[x_index], set_of_two[0]
    # print(possible_combinations_of_five_cards)
    combination_numbers = [evaluate_combination_of_five_cards(i) for i in possible_combinations_of_five_cards]
    return min(combination_numbers)


class Combination:
    __combination_inst = None

    @staticmethod
    def get_instance():
        if Combination.__combination_inst is None:
            Combination()
        return Combination.__combination_inst

    def __init__(self):
        if Combination.__combination_inst is not None:
            raise Exception("Error:: multiple combination objects")
        else:
            self.__players_cards = {}
            self.__cards_on_table = []
            # self.__combinations = {}
            Combination.__combination_inst = self

    def compute_combinations(self):
        for player in self.__players_cards.keys():
            card_combination = self.__players_cards.get(player) + self.__cards_on_table
            player.set_cards_combination_number(get_card_combination_number(card_combination))

    # def get_player_combination_number(self, player: Player) -> float:
    #     return self.__combinations[player]
    #
    # def get_combinations(self) -> dict:
    #     return self.__combinations

    def set_cards_on_table(self, cards_on_table: list):
        self.__cards_on_table = cards_on_table

    def set_players_cards(self, players_cards: dict):
        self.__players_cards = players_cards
