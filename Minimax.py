import Evaluators
import random

# Default max depth
MAXDEPTH = 2
# Default evaluation function
DEFAULTEVAL = Evaluators.numEnemies

class MinimaxAgent:
    def __init__(self, stateBelief, eval=DEFAULTEVAL, maxdepth=MAXDEPTH):
        # Takes what the AI believes the board is as a state
        self._state = stateBelief
        self._eval = eval
        self._maxdepth = maxdepth
    
    def getMove(self):
        return self.runMinimax(self._state, 0, "max")[0]
    
    def runMinimax(self, board, depth, minOrMax):
        if depth == self._maxdepth:
            return None, self._eval(board, minOrMax=minOrMax)
        else:
            moves = board.getValidMoves()
            if len(moves) == 0:
                # Special lose case
                return None, self._eval(None, result="LOSE", minOrMax=minOrMax)
            moveEvals = []

            for move in moves:
                moveEvals.append((move, self.runMinimax(board.nextState(move)[0], depth + 1, "min" if minOrMax=="max" else "max")[1]))
            bestMove = [moveEvals[0]]
            bestVal = moveEvals[0][1]
            for move in moveEvals:
                if move[1] > bestVal:
                    bestMove = [move]
                    bestVal = move[1]
                elif move[1] == bestVal:
                    bestMove.append(move)
            bm = random.choice(bestMove)
            return bm[0], bm[1]
            


