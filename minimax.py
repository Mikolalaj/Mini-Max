
from games.dots_and_boxes import DotsAndBoxes, DotsAndBoxesMove

def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        return position.get_value()

    if maximizingPlayer:
        value = -float('inf')
        for move in position.legal_moves():
            value = max(value, minimax(move, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    if not maximizingPlayer:
        value = float('inf')
        for move in position.legal_moves():
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
        self.add_childs()
    
    def add_child(self, child):
        self.childs.append(child)
    
    def add_childs(self):
        print(self.game)
        print(self.game.is_finished())
        print(self.game.get_moves())
        if self.game.is_finished() == False:
            for move in self.game.get_moves():
                game_copy = self.game
                game_copy.make_move(move)
                self.add_child(Position(game_copy))
        else:
            if self.game.get_winner() == None:
                self.value = 0
            elif self.game.get_winner().char == '1':
                self.value = 1
            else:
                self.value = -1

game = DotsAndBoxes(2)
game.make_move(DotsAndBoxesMove('v', (0, 0)))
game.make_move(DotsAndBoxesMove('h', (0, 0)))
game.make_move(DotsAndBoxesMove('v', (1, 0)))
game.make_move(DotsAndBoxesMove('h', (1, 2)))
game.make_move(DotsAndBoxesMove('h', (0, 2)))
game.make_move(DotsAndBoxesMove('v', (1, 2)))
game.make_move(DotsAndBoxesMove('v', (0, 2)))
game.make_move(DotsAndBoxesMove('h', (1, 0)))
game.make_move(DotsAndBoxesMove('h', (1, 1)))

positions = Position(game)