# def get_card_combination_number(card_combination: list) -> list:
#     possible_combinations_of_five_cards = []
#     set_of_five = card_combination[:5]
#     set_of_two = card_combination[5:]
#     print(set_of_five)
#     print(set_of_two)
#     possible_combinations_of_five_cards.append(set_of_five.copy())
#
#     """Each out of 2"""
#     for i in range(len(set_of_two)):
#         for k in range(len(set_of_five)):
#             set_of_two[i], set_of_five[k] = set_of_five[k], set_of_two[i]
#             print(set_of_five, set_of_two)
#             possible_combinations_of_five_cards.append(set_of_five.copy())
#             print(possible_combinations_of_five_cards)
#             set_of_two[i], set_of_five[k] = set_of_five[k], set_of_two[i]
#
#     """Both out of 2 (x, y) = set_of_two"""
#     offset = 1
#     for x_index in range(4):
#         set_of_two[0], set_of_five[x_index] = set_of_five[x_index], set_of_two[0]
#         for y_index in range(5-offset):
#             set_of_two[1], set_of_five[y_index + offset] = set_of_five[y_index + offset], set_of_two[1]
#             possible_combinations_of_five_cards.append(set_of_five.copy())
#             set_of_two[1], set_of_five[y_index + offset] = set_of_five[y_index + offset], set_of_two[1]
#         offset += 1
#         set_of_two[0], set_of_five[x_index] = set_of_five[x_index], set_of_two[0]
#     return possible_combinations_of_five_cards
#
#
# arr = [0, 1, 2, 3, 4, 5, 6]
# print(get_card_combination_number(arr))
# combination_numbers = {player+90: player for player in arr}
# print(combination_numbers)
# dic = {
#     "r": 9,
#     "t": 2,
#     "p": 4,
#     "o": 8,
# }
#
# print({k: v for k, v in sorted(dic.items(), key=lambda item: item[1])})
from Poker import Poker
from main_classes.Player import Player

poker = Poker.get_instance()

print(Poker.get_instance())

players = [Player("Boris", 1, 200), Player("Alice", 2, 200), Player("Felix", 3, 200)]

poker.add_players(players)
print("======Game setup======")
poker.game_setup(10)
print(poker.get_table())
print("======Round 2======")
poker.round()
print(poker.get_table())
print("======Round 3======")
poker.round()
print(poker.get_table())
poker.end_round()






# i = 0
# arr = [0, 1, 1]
# arr1 = [9, 9]
# for _ in range(10):
#     i = (i + 1) % len(arr)
# print(arr+arr1)
