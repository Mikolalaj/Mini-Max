
from minimax import minimax, GameTree
from games.dots_and_boxes import DotsAndBoxes, DotsAndBoxesMove


BOARD_SIZE = 2
MOVES = [
    ('v', (0, 0)), ('v', (1, 2)), ('v', (1, 0)),
    ('v', (0, 2)), ('h', (0, 0)), ('h', (1, 2))
]

game = DotsAndBoxes(BOARD_SIZE)
for move in MOVES:
    game.make_move(DotsAndBoxesMove(*move))

print('Starting Board\n')
print(game, '\n')

game_tree = GameTree(game)

result = minimax(game_tree, True if game_tree.game.get_current_player().char == '1' else False)

if result == 1:
    print('Player 1 wins')
elif result == -1:
    print('Player 2 wins')
elif result == 0:
    print('It\'s a draw!')
else:
    print('Error!')
