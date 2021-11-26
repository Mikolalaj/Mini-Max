
from copy import deepcopy
from games.dots_and_boxes import DotsAndBoxes, DotsAndBoxesMove

def minimax(position, depth, maximizingPlayer, alpha=-float('inf'), beta=float('inf')):
    if depth == 0:
        return position.get_value()

    if maximizingPlayer:
        value = -float('inf')
        for move in position.get_moves():
            value = max(value, minimax(move, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    if not maximizingPlayer:
        value = float('inf')
        for move in position.get_moves():
            value = min(value, minimax(move, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


class Position:
    def __init__(self, game) -> None:
        self.game = game
        self.value = None
        self.childs = []
        self.depth = 0
        self.add_childs()
        
    def add_childs(self):
        if self.game.is_finished() == False:
            for move in self.game.get_moves():
                game_copy = deepcopy(self.game)
                game_copy.make_move(move)
                self.childs.append(Position(game_copy))
                if self.childs[-1].depth + 1 > self.depth:
                    self.depth = self.childs[-1].depth + 1
        else:
            self.depth = 0
            winner = self.game.get_winner()
            if winner == None:
                self.value = 0
            elif winner.char == '1':
                self.value = 1
            elif winner.char == '2':
                self.value = -1
    
    def get_value(self):
        return self.value

    def get_moves(self):
        return self.childs

game = DotsAndBoxes(2)
game.make_move(DotsAndBoxesMove('v', (0, 0)))
game.make_move(DotsAndBoxesMove('v', (1, 2)))
game.make_move(DotsAndBoxesMove('v', (1, 0)))
game.make_move(DotsAndBoxesMove('v', (0, 2)))

print(game, '\n')

positions = Position(game)

starting_player = True if positions.game.get_current_player().char == '1' else False
result = minimax(positions, positions.depth, starting_player)
print(result)
if result == 1:
    print('Player 1 wins')
elif result == -1:
    print('Player 2 wins')
else:
    print('It\'s a draw!')
