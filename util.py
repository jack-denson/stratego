import Piece

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