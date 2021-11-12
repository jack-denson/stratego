import GameState
import random
import Piece
import Player

def randomGame():
    state = GameState.GameState()

    for i in range(10):
        if i%2 == 0:
            state.show(False)
        moves = state.getValidMoves()
        move = random.choice(moves)
        state, battleInfo = state.nextState(move)
        if len(battleInfo) > 0:
            print(battleInfo[0] + " attacks " + battleInfo[1])
        print(move.toStr())

def singlePiece():
    board = [[None for i in range(10)] for j in range(10)]
    # Fill in the water squares
    board[4][2] = "W"
    board[5][2] = "W"
    board[4][3] = "W"
    board[5][3] = "W"
    board[4][6] = "W"
    board[5][6] = "W"
    board[4][7] = "W"
    board[5][7] = "W"
    player = Player.AI()
    board[1][1] = Piece.Piece("5", player)
    state = GameState.GameState(board=board, players=[player, Player.AI()])
    for i in state.getValidMoves():
        print(i.toStr())
    state.show()

randomGame()
