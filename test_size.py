import timeit
import matplotlib.pyplot as plt
from minimax import minimax, GameTree
from games.dots_and_boxes import DotsAndBoxes, DotsAndBoxesMove


def code(board_size):

    game = DotsAndBoxes(board_size)
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


x_axis = []
y_axis = []

for i in range(2, 11):
    t = timeit.Timer(lambda: code(i)) 
    result = t.timeit(1)
    x_axis.append(i)
    y_axis.append(result)

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
ax.set_ylabel('Czas działania (s)')
ax.set_xlabel('Wielkość planszy')
ax.set_title('Czas działania algorytmu w zależności od wielkości planszy')
plt.show()

