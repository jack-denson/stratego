# Different evaluation functions
# Assumes player 0 is maximizing, player 1 is minimizing

def numEnemies(state, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40
    """if minOrMax == "max":
        opponent = state.getPlayer(1)
    else:
        assert(minOrMax == "min")
        opponent = state.getPlayer(0)"""
    minimizer = state.getPlayer(1)
    
    board = state.getBoard()
    totalEnemies = 0
    for i in range(10):
        for j in range(10):
            if not (board[i][j] is None or board[i][j] == "W" or board[i][j].getPlayer() != minimizer):
                totalEnemies += 1
    
    return -1 * totalEnemies

# Number of flags - although there is always one flag, because of belief, we have a few that COULD be flags, minimize
#   how many of those there are(i.e., attack the flags)
def numFlags(state, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40
    if minOrMax == "max":
        opponent = state.getPlayer(1)
    else:
        assert(minOrMax == "min")
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


# Corresponds to "take random move, all states are the same"
def nullEval(state, result="CONTINUE", minOrMax="max"):
    return 0


evalMap = {"numEnemies": numEnemies, 
            "null": nullEval, 
            "none": nullEval,
            "nullEval": nullEval,
            "flags": numFlags, 
            "numFlags": numFlags, 
            None: None}