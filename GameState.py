import Player

class GameState:
    def __init__(self, board=None, players=[Player.AI(), Player.AI()], turn=0):
        self._players = players
        self._turn = turn

        if board is None:
            self._board = [[None for i in range(10)] for j in range(10)]
            # Fill in the water squares
            self._board[4][2] = "W"
            self._board[5][2] = "W"
            self._board[4][3] = "W"
            self._board[5][3] = "W"
            self._board[4][6] = "W"
            self._board[5][6] = "W"
            self._board[4][7] = "W"
            self._board[5][7] = "W"

            p0Pieces = self._players[0].setPieces()
            p1Pieces = self._players[1].setPieces()

            for i in range(4):
                for j in range(10):
                    self._board[3-i][9-j] = p0Pieces[i][j]
                    self._board[6 + i][j] = p1Pieces[i][j]

        else:
            self._board = board

    def show(self, all=False):
        print(self._board[0] == self._board[1])
        for i in range(0, 10):
            print("|", end="")
            for j in range(0, 10):
                if self._board[i][j] is None:
                    print("  ", end="")
                elif self._board[i][j] == "W":
                    print(" W", end="")
                elif not all and self._board[i][j].getPlayer() != self._players[self._turn]:
                    print(" ?", end="")
                else:
                    print(" "+self._board[i][j].getType(), end="")
                print(" |", end="")
            print()


