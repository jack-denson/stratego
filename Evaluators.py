# Different evaluation functions
# Assumes player 0 is maximizing, player 1 is minimizing

def numEnemies(state, result="CONTINUE", minOrMax="max"):
    if result == "LOSE":
        return -40 if minOrMax=="max" else 40
    if minOrMax == "max":
        opponent = state.getPlayer(1)
    else:
        assert(minOrMax == "min")
        opponent = state.getPlayer(0)
    
    board = state.getBoard()
    totalEnemies = 0
    for i in range(10):
        for j in range(10):
            if not (board[i][j] is None or board[i][j] == "W" or board[i][j].getPlayer() != opponent):
                totalEnemies += 1
    
    if minOrMax == "min":
        return totalEnemies
    else:
        return -1*totalEnemies