
from minimax import minimax, GameTree
from games.dots_and_boxes import DotsAndBoxes, DotsAndBoxesMove

game = DotsAndBoxes(2)

moves = [
    ('v', (0, 0)), ('v', (1, 2)), ('v', (1, 0)),
    ('v', (0, 2)), ('h', (0, 0)), ('h', (1, 0)),
    ('v', (1, 1)), ('h', (0, 1)), ('h', (1, 1)),
    ('h', (0, 2)), ('h', (1, 2)), ('v', (0, 1)),
    
]

for move in moves:
    game.make_move(DotsAndBoxesMove(*move))

print(game)

game_tree = GameTree(game)

result = minimax(game_tree, True if game_tree.game.get_current_player().char == '1' else False)

if result == 1:
    print('Player 1 wins')
elif result == -1:
    print('Player 2 wins')
elif result == 0:
    print("It's a draw!")
else:
    print('Error!')
