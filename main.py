
from minimax import minimax, GameTree
from games.dots_and_boxes import DotsAndBoxes, DotsAndBoxesMove

game = DotsAndBoxes(2)

moves = [
    ('v', (0, 0)), ('v', (1, 2)), ('v', (1, 0)),
    ('v', (0, 2)), ('h', (0, 0)), ('h', (1, 0)),
    ('v', (1, 1)), ('h', (0, 1)), ('h', (1, 1))
]

# moves = [
#     ('v', (1, 1)), ('v', (0, 0)), ('v', (1, 0)),
#     ('v', (0, 1)), ('h', (0, 0)), ('h', (1, 0))
# ]

for move in moves:
    game.make_move(DotsAndBoxesMove(*move))

print(game)

game_tree = GameTree(game)

result = minimax(game_tree, True if game_tree.game.get_current_player().char == '1' else False)

winners = [game_result.value for game_result in game_tree.childs]
# print(winners)

current_game = game_tree.game

if current_game.get_current_player().char == '1':
    best_move = current_game.get_moves()[winners.index(max(winners))]
else:
    best_move = current_game.get_moves()[winners.index(min(winners))]

current_game.make_move(best_move)

print('\nBest next move', str(current_game)[17:], '\n')


if result == 1:
    print('Player 1 wins')
elif result == -1:
    print('Player 2 wins')
elif result == 0:
    print("It's a draw!")
else:
    print('Error!')
