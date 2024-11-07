class Game:
    def __init__(self):
        self.turn = 'X' # Turn
        self.tie= False # Tie status
        self.winner = None # Winner Status
        self.board = { # Board Layout
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    def play_game(self):
        print("play that tic tac toe type beat")
        # Game Logic, place holder for now
    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    def print_message(self):
        if self.tie:
            print("Tieee game!")
        elif self.winner:
            print(f"{self.winner} is the winner!")
        else:
            print(f"{self.turn}'s turn!")
    def get_move(self):
        while True:
            move = input("Enter your move:(example: A1)").lower() #converts to lowercase to avoid errors
            if move in self.board and self.board[move] is None: #checks if move is valid and not taken
                self.board[move] = self.turn #if valid, places move on board
                break
            else:
                print("Invalid move, try again.") #invalid move, print & continue loop

game_instance = Game()
game_instance.play_game()