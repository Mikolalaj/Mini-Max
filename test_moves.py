import timeit
import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from minimax import minimax, GameTree
from games.dots_and_boxes import DotsAndBoxes


def code(game):
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


game = DotsAndBoxes(4)
all_moves = game.get_moves()
moves_count = len(all_moves)

results = []

for _ in range(20):
    moves = deepcopy(all_moves)
    game_copy = deepcopy(game)
    y_axis = []

    i=0
    while moves != []:
        next_move = moves.pop(random.randint(0, len(moves)-1))
        t = timeit.Timer(lambda: code(game_copy))
        result = t.timeit(1)
        y_axis.append(result)
        
        game_copy.make_move(next_move)
        i+=1
    results.append(y_axis)
    del game_copy


average = []

for i in range(len(results[0])):
    total = 0
    for j in range(len(results)):
        total += results[j][i]
    average.append(total/len(results))

x_axis = [i for i in range(1, moves_count+1)]

fig, ax = plt.subplots()
ax.plot(x_axis, average)
ax.set_ylabel('Czas działania (s)')
ax.set_xlabel('Ilośc wykonanych ruchów')
ax.set_title('Czas działania algorytmu w zależności od wykonanych ruchów')
plt.show()
