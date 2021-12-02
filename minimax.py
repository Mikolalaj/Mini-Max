
from copy import deepcopy
from games.dots_and_boxes import DotsAndBoxes


class GameTree:
    def __init__(self, game: DotsAndBoxes) -> None:
        self.game = game
        self.moves = self.game.get_moves()
        self.childs = []
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
            new_game_tree = GameTree(game_copy)
            self.childs.append(new_game_tree)
            return new_game_tree
    
    def get_current_player(self) -> bool:
        return True if self.game.get_current_player().char == '1' else False


def minimax(game_tree: GameTree, maximizingPlayer: bool, alpha=-float('inf'), beta=float('inf')):
    value = game_tree.get_value()
    if value is not None:
        return value

    if maximizingPlayer:
        best_value = -float('inf')
        while len(game_tree.moves) != 0:
            child = game_tree.get_next_child()
            next_player = child.get_current_player()
            best_value = max(best_value, minimax(
                child, next_player, alpha, beta))
            alpha = max(alpha, best_value)
            child.value = best_value
            if beta <= alpha:
                break
        return best_value

    if not maximizingPlayer:
        best_value = float('inf')
        while len(game_tree.moves) != 0:
            child = game_tree.get_next_child()
            next_player = child.get_current_player()
            best_value = min(best_value, minimax(
                child, next_player, alpha, beta))
            beta = min(beta, best_value)
            child.value = best_value
            if beta <= alpha:
                break
        return best_value
