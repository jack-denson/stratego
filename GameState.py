import Move
import Player

class GameState:
    def __init__(self, board=None, players=[None, None], turn=0):
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

            self._players[0].initState(self)
            self._players[1].initState(self)

        else:
            self._board = [[(board[i][j] if board[i][j] == "W" or board[i][j] is None else board[i][j].copy()) for j in range(10)] for i in range(10)]
    
    def getBoard(self):
        return self._board

    def show(self, all=False, color=True):

        print(" ", end="")
        for letter in " ABCDEFGHIJ":
            print(" " + letter + " |", end="")
        print("\n     "+("_"*40))
        # 0 is blue, 1 is red
        endcode = '' if not color else '\033[0m'
        for i in range(0, 10):
            print("| "+str(i)+" |", end="")
            for j in range(0, 10):
                if self._board[i][j] is None:
                    print("  ", end="")
                elif self._board[i][j] == "W":
                    print(" W", end="")
                elif self._board[i][j].getPlayer() != self._players[self._turn]:
                    # Here, drawing opponent(not this turn)'s piece
                    colorcode = '' if not color else ('\033[31m' if self._turn == 0 else '\033[94m')
                    if not all:
                        print(" "+colorcode+"?"+endcode, end="")
                    else:
                        print(" " + colorcode + self._board[i][j].getType() + endcode, end="")
                else:
                    colorcode = '' if not color else ('\033[94m' if self._turn == 0 else '\033[31m')
                    print(" " + colorcode + self._board[i][j].getType() + endcode, end="")
                print(" |", end="")
            print()

    def currentPlayer(self):
        return self._players[self._turn]

    def getPlayer(self, playerNum):
        return self._players[playerNum]

    def getValidMoves(self):
        # Returns all valid moves for a state
        validMoves = []
        for i in range(10):
            for j in range(10):
                piece = self._board[i][j]
                if piece is not None and piece != "W" and piece.getPlayer() == self.currentPlayer() and piece.canMove():
                    # We've found one of our movable pieces
                    if piece.getType() == "9":
                        # Do rook stuff
                        #Check vertical
                        for dir in [1, -1]:
                            done = False
                            dist = 1
                            while not done:
                                move = Move.Move(i, j, i + dir*dist, j)
                                if self.isValid(move):
                                    validMoves.append(move)
                                else:
                                    done = True
                                dist += 1
                        #Check horizontal
                        for dir in [1, -1]:
                            done = False
                            dist = 1
                            while not done:
                                move = Move.Move(i, j, i, j + dir*dist)
                                if self.isValid(move):
                                    validMoves.append(move)
                                else:
                                    done = True
                                dist += 1
                    else:
                        for dir in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            move = Move.Move(i, j, i + dir[0], j + dir[1])
                            if self.isValid(move):
                                #print(self._board[i][j].getType(), "from", i, j, " -> ", i+ydir, j+xdir)
                                validMoves.append(move)

        return validMoves

    def isValid(self, move):
        r0, c0 = move.getStart()
        r1, c1 = move.getEnd()


        # Check for OOB stuff
        if min(r0, c0, r1, c1) < 0:
            return False
        if max(r0, c0, r1, c1) > 9:
            return False


        piece = self._board[r0][c0]
        destination = self._board[r1][c1]

        if piece is None or piece == "W" or not piece.canMove() or destination == "W" or \
                (destination is not None and destination.getPlayer() == self._players[self._turn]) or \
                piece.getPlayer() != self._players[self._turn]:
            # If there's no piece there, or the piece is immobile, or the destination is water, or the destination has
            #  a teammate in it, or the piece isn't our piece, move is invalid
            return False

        if piece.getType() == "9":
            # Scout moves like a chess rook
            if r1 == r0 and c0 != c1:
                start = min(c0, c1)
                stop = max(c0, c1)
                for i in range(start+1, stop):
                    if self._board[r0][i] is not None:
                        return False
                return True
            elif c1 == c0 and r0 != r1:
                start = min(r0, r1)
                stop = max(r0, r1)
                for i in range(start+1, stop):
                    if self._board[i][c0] is not None:
                        return False
                return True
            return False
        else:
            return (r1 == r0 and abs(c0 - c1) == 1) or (c1 == c0 and abs(r0 - r1) == 1)

    def nextState(self, move):
        # The state of the game if a move is taken. Presumes move has already been checked for validity
        r0, c0 = move.getStart()
        r1, c1 = move.getEnd()
        startPiece = self._board[r0][c0]
        endPiece = self._board[r1][c1]

        nextBoard = [[self._board[i][j] for j in range(10)] for i in range(10)]

        battleInfo = []
        if endPiece is None:
            nextBoard[r1][c1] = startPiece
            nextBoard[r0][c0] = None
        else:
            # If we have a battle, we need to send that info along
            battleInfo = [startPiece.getType(), endPiece.getType()]
            if startPiece.beats(endPiece):
                nextBoard[r1][c1] = startPiece
                nextBoard[r0][c0] = None
            elif endPiece.beats(startPiece):
                nextBoard[r0][c0] = None
            else:
                # If ranks are equal, they both die
                nextBoard[r1][c1] = None
                nextBoard[r0][c0] = None

        return GameState(board=nextBoard, players=self._players, turn= (-1*self._turn + 1)), battleInfo


