
from copy import deepcopy
from games.dots_and_boxes import DotsAndBoxes


class GameTree:
    def __init__(self, game: DotsAndBoxes) -> None:
        self.game = game
        self.moves = self.game.get_moves()
        if self.moves == []:
            winner = self.game.get_winner()
            if winner == None:
                self.value = 0
            elif winner.char == '1':
                self.value = 1
            elif winner.char == '2':
                self.value = -1
        else:
            self.value = None
    
    def get_value(self):
        return self.value

    def get_next_child(self):
        if len(self.moves) == 0:
            return None
        else:
            game_copy = deepcopy(self.game)
            next_move = self.moves.pop(0)
            game_copy.make_move(next_move)
            return GameTree(game_copy)


def minimax(game_tree: GameTree, maximizingPlayer: bool, alpha=-float('inf'), beta=float('inf')):
    value = game_tree.get_value()
    if value is not None:
        return value

    if maximizingPlayer:
        value = -float('inf')
        while len(game_tree.moves) != 0:
            position_child = game_tree.get_next_child()
            value = max(value, minimax(position_child, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    if not maximizingPlayer:
        value = float('inf')
        while len(game_tree.moves) != 0:
            position_child = game_tree.get_next_child()
            value = min(value, minimax(position_child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


