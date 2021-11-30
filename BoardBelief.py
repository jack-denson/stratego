import PieceBelief
import util
# A belief for an entire board, that is, a probability distribution for each opponent's piece
class BoardBelief:

    def __init__(self, state, player):
        # Pieces remaining in play
        self._player = player
        self._opRemaining = {
            '1': 1,
            '2': 1,
            '3': 2,
            '4': 3,
            '5': 4,
            '6': 4,
            '7': 4,
            '8': 5,
            '9': 8,
            'S': 1,
            'F': 1,
            'B': 6
        }

        # Pieces in play that we aren't 100% about
        self._opUnaccounted = self._opRemaining.copy()


        # A convenience array of the piece beliefs
        self._opPieces = []

        stateBoard = state.getBoard()
        self._board = [[None for i in range(10)] for j in range(10)]
        for i in range(len(stateBoard)):
            for j in range(len(stateBoard[i])):
                if stateBoard[i][j] is None or stateBoard[i][j] == "W":
                    self._board[i][j] = stateBoard[i][j]
                elif stateBoard[i][j].getPlayer() == player:
                    self._board[i][j] = stateBoard[i][j].copy()
                else:
                    self._board[i][j] = PieceBelief.PieceBelief()
                    self._opPieces.append(self._board[i][j])

    def updateFromRemaining(self):
        for pieceBelief in self._opPieces:
            pieceBelief.updateFromRemaing(self._opUnaccounted)

    def printBelief(self, color=True):
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
                elif isinstance(self._board[i][j], PieceBelief.PieceBelief):
                    colorcode = '' if not color else ('\033[31m')
                    print(" " + colorcode + self._board[i][j].mostLikely() + endcode, end="")
                else:
                    colorcode = '' if not color else ('\033[94m')
                    print(" " + colorcode + self._board[i][j].getType() + endcode, end="")
                print(" |", end="")
            print("    BELIEVED")

    def observeMove(self, player, move, battleInfo):
        # If we become certain about a piece, update all other pieces
        # P(P1=X | P2 = Y) = P(p2 = Y | p1= X) * P(p1 = X)
        # Set prob for each = b.o Dist if p1=X * prob already stored

        if len(battleInfo) > 0:
            opPiece = (battleInfo[1], move.getEnd()) if player==self._player else (battleInfo[0], move.getStart())
            if not self._board[opPiece[1][0]][opPiece[1][1]].isCertain():
                for piece in self._opPieces:
                    if not piece.isCertain() and not self._board[opPiece[1][0]][opPiece[1][1]] == piece:
                        piece.updateProbFromCert(self._opUnaccounted, opPiece[0])
                self._opUnaccounted[opPiece[0]] = self._opUnaccounted[opPiece[0]] - 1
                self._board[opPiece[1][0]][opPiece[1][1]].certain(opPiece[0])
            
            # Now update board to reflect
            r0, c0 = move.getStart()
            r1, c1 = move.getEnd()
            if util.beats(battleInfo[0], battleInfo[1]):
                self._board[r1][c1] = self._board[r0][c0]
                self._board[r0][c0] = None
                if player == self._player:
                    # Remove from opRemaining if it's the opponent's
                    self._opRemaining[battleInfo[1]] = self._opRemaining[battleInfo[1]] - 1
            elif util.beats(battleInfo[1], battleInfo[0]):
                self._board[r0][c0] = None
                if player != self._player:
                    # Remove from opRemaining if it's the opponent's
                    self._opRemaining[battleInfo[0]] = self._opRemaining[battleInfo[0]] - 1
            else:
                # If ranks are equal, they both die
                self._board[r1][c1] = None
                self._board[r0][c0] = None
                self._opRemaining[battleInfo[0]] = self._opRemaining[battleInfo[0]] - 1
                self._opRemaining[battleInfo[1]] = self._opRemaining[battleInfo[1]] - 1
        else:
            r0, c0 = move.getStart()
            r1, c1 = move.getEnd()
            self._board[r1][c1] = self._board[r0][c0]
            self._board[r0][c0] = None
