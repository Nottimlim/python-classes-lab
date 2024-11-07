class Game:
    def __init__(self):
        self.turn = 'X' // Turn
        self.tie= False // Tie status
        self.winner = None // Winner Status
        self.board = { // Board Layout
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }