import PieceBelief

# A belief for an entire board, that is, a probability distribution for each opponent's piece
class BoardBelief:

    def __init__(self, state, player):
        # Pieces remaining in play
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
                    self._board[i][j] = PieceBelief()
                    self._opPieces.append(self._board[i][j])

    def updateFromRemaining(self):
        for pieceBelief in self._opPieces:
            pieceBelief.updateFromRemaing(self._opUnaccounted)

    

