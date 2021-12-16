# Different evaluation functions
# Assumes player 0 is maximizing, player 1 is minimizing
import util


def numEnemies(state, maximizer, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40
    """if minOrMax == "max":
        opponent = state.getPlayer(1)
    else:
        assert(minOrMax == "min")
        opponent = state.getPlayer(0)"""
    
    if (minOrMax == "max" and state.getPlayer(1) == maximizer) or (minOrMax == "min" and state.getPlayer(1) != maximizer):
        opponent = state.getPlayer(1)
    else:
        opponent = state.getPlayer(0)
    
    board = state.getBoard()
    totalEnemies = 0
    for i in range(10):
        for j in range(10):
            if not (board[i][j] is None or board[i][j] == "W" or board[i][j].getPlayer() != opponent):
                totalEnemies += 1
    
    return -1 * totalEnemies

# Number of flags - although there is always one flag, because of belief, we have a few that COULD be flags, minimize
#   how many of those there are(i.e., attack the flags)
def numFlags(state, maximizer, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40
    if (minOrMax == "max" and state.getPlayer(1) == maximizer) or (minOrMax == "min" and state.getPlayer(1) != maximizer):
        opponent = state.getPlayer(1)
    else:
        opponent = state.getPlayer(0)
    
    
    board = state.getBoard()
    totalFlags = 0
    for i in range(10):
        for j in range(10):
            if not (board[i][j] is None or board[i][j] == "W" or board[i][j].getPlayer() != opponent):
                totalFlags += 1 if board[i][j].getType() == "F" else 0
    
    if minOrMax == "min":
        return totalFlags
    else:
        return -1*totalFlags

def flagsAndBombs(state, maximizer, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40

    if (minOrMax == "max" and state.getPlayer(1) == maximizer) or (minOrMax == "min" and state.getPlayer(1) != maximizer):
        opponent = state.getPlayer(1)
    else:
        opponent = state.getPlayer(0)

    board = state.getBoard()
    totalFnB = 0
    for i in range(10):
        for j in range(10):
            if not (board[i][j] is None or board[i][j] == "W" or board[i][j].getPlayer() == opponent):
                totalFnB += 1 if (board[i][j].getType() == "F" or board[i][j].getType() == "B") else 0
    
    return -1 * totalFnB

def targetBombs(state, maximizer, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40

    # -10 for each enemy bomb, plus average min bomb-miner distance(manhattan)
    board = state.getBoard()

    bombs = []
    miners = []
    value = 0

    if (minOrMax == "max" and state.getPlayer(1) == maximizer) or (minOrMax == "min" and state.getPlayer(1) != maximizer):
        opponent = state.getPlayer(1)
    else:
        opponent = state.getPlayer(0)

    for i in range(10):
        for j in range(10):
            if not (board[i][j] is None or board[i][j] == "W"):
                if board[i][j].getType() == "B" and board[i][j].getPlayer() == opponent:
                    bombs.append((i, j))
                elif board[i][j].getType() == "8" and board[i][j].getPlayer() != opponent:
                    miners.append((i, j))

    if len(bombs) == 0:
        value = 40
    if len(miners) == 0:
        value = -40

    if value == 0:
        dists = []
        for bomb in bombs:
            minDist = None
            for miner in miners:
                if minDist is None or util.manhattan(bomb, miner) < minDist:
                    minDist = util.manhattan(bomb, miner)
            dists.append(minDist)
        
        avgDist = util.mean(dists)

        value -= 2 * avgDist - 10 * len(bombs)

    if minOrMax == "min":
        return -1 * value
    else:
        return value
    
def justMoveForward(state, maximizer, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return 0 if minOrMax=="max" else 11
    #Literally just average y position of all pieces
    sum = 0
    num = 0
    for i in range(10):
        for j in range(10):
            if not (state.getBoard()[i][j] is None or state.getBoard()[i][j] == "W"):
                num += 1
                sum += i
    
    return (1 if maximizer == state.getPlayer(1) else -1) * sum / num

# Corresponds to "take random move, all states are the same"
def nullEval(state, player, result="CONTINUE", minOrMax="max"):
    return 0


evalMap = {"numEnemies": numEnemies, 
            "null": nullEval, 
            "none": nullEval,
            "nullEval": nullEval,
            "flags": numFlags, 
            "numFlags": numFlags, 
            "fnb": flagsAndBombs,
            "flagsAndBombs": flagsAndBombs,
            "targetBombs": targetBombs,
            "bombs": targetBombs,
            "forward": justMoveForward,
            "fwd": justMoveForward,
            "justMoveForward": justMoveForward,
            None: None}