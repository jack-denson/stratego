# Default max depth
MAXDEPTH = 4
DEFAULTEVAL = None

class MinimaxAgent:
    def __init__(self, stateBelief, eval=DEFAULTEVAL, maxdepth=MAXDEPTH):
        # Takes what the AI believes the board is as a state
        self._state = stateBelief
        self._eval = eval
        self._maxdepth = maxdepth
    
    def getMove(self):
        self.runMinimax(self._board, 0, "max")
    
    def runMinimax(self, board, depth, minOrMax):
        if depth == self._maxdepth:
            return None, self._eval(board)
        else:
            moves = self._state.getValidMoves()
            if len(moves) == 0:
                # Special lose case
                return self._eval(None, result="LOSE", minOrMax=minOrMax)
            moveEvals = []
            for move in moves:
                moveEvals.append((move, self.runMinimax(board.nextState(move), depth + 1, "min" if minOrMax=="max" else "max")))
            bestMove = moveEvals[0]
            for move in moveEvals:
                if move[1] > bestMove[1]:
                    bestMove = move
            
            return bestMove[0], bestMove[1]
            


