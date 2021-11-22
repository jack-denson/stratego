import Piece
import random

def startPieces(player):
    #Flat array of all 40 starting pieces, for a given player
    bombs = [Piece.Piece("B", player) for i in range(6)]
    marshal = [Piece.Piece("1", player)]
    general = [Piece.Piece("2", player)]
    colonels = [Piece.Piece("3", player) for i in range(2)]
    majors = [Piece.Piece("4", player) for i in range(3)]
    captains = [Piece.Piece("5", player) for i in range(4)]
    lieuts = [Piece.Piece("6", player) for i in range(4)]
    sarges = [Piece.Piece("7", player) for i in range(4)]
    miners = [Piece.Piece("8", player) for i in range(5)]
    scouts = [Piece.Piece("9", player) for i in range(8)]
    spies = [Piece.Piece("S", player)]
    flag = [Piece.Piece("F", player)]
    pieces = bombs + marshal + general + colonels + majors + captains \
             + lieuts + sarges + miners + scouts + spies + flag
    assert(len(pieces) == 40)
    return pieces

def setupFromString(player, setup):
    #Parses string like B321FS3209583B... to 4x10 array of pieces
    configuration = []
    for r in range(4):
        row = []
        for c in range(10):
            row.append(Piece.Piece(setup[r*10 + c], player))
        configuration.append(row)
    return configuration

def wikipediaSetup(player):
    # Example setup that the wikipedia article for Stratego shows
    return setupFromString(player, "7B5299189BB79S4585397B48643876BFB5966998")

def validPos(pos):
    pos = pos.lower()
    return "abcdefghij".find(pos[0]) != -1 and "0123456789".find(pos[1]) != -1

def toCoords(pos):
    pos = pos.lower()
    row = int(pos[1])
    col = "abcdefghij".index(pos[0])
    return row, col

def toUserCoord(row, col):
    return "ABCDEFGHIJ"[col] + str(row)

def randomMove(state):
    moves = state.getValidMoves()
    if len(moves) == 0:
        return None
    move = random.choice(moves)
    return move