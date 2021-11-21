

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
    def __init__(self, childs, value=None) -> None:
        self.value = value
        self.childs = childs

    def legal_moves(self) -> list:
        return self.childs

    def get_value(self) -> int:
        return self.value


game = Position([
    Position([
        Position([
            Position([], -2),
            Position([], 3)
        ]),
        Position([
            Position([], -5),
            Position([], 2)
        ])
    ]),
    Position([
        Position([
            Position([], 4),
            Position([], -8)
        ]),
        Position([
            Position([], -20),
            Position([], 1)
        ])
    ])
])


print(minimax(game, 3, -float('inf'), float('inf'), True))
