
import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from minimax import minimax, GameTree
from games.dots_and_boxes import DotsAndBoxes


def code(game):
    game_tree = GameTree(game)

    minimax(game_tree, True if game_tree.game.get_current_player().char == '1' else False)

    return game_tree.get_size()
    


game = DotsAndBoxes(4)
all_moves = game.get_moves()
moves_count = len(all_moves)

x_axis = []
y_axis = []

i = 0
while all_moves != []:
    next_move = all_moves.pop(random.randint(0, len(all_moves)-1))
    
    y_axis.append(code(game))
    x_axis.append(i)
    game.make_move(next_move)
    i += 1

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
ax.set_ylabel('Ilość wierzchołków drzewa')
ax.set_xlabel('Ilośc wykonanych ruchów')
ax.set_title('Wielkość drzewa gry w zależności od wykonanych ruchów')
plt.show()
