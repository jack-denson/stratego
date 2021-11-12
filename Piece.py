
class Piece:

    def __init__(self, type, player):
        assert(type in {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'F', 'B'})
        self._type = type
        self._player = player

    def getType(self, restrict=None):
        # Restrict is used to ensure player only accesses their pieces, field should be player's self when this func.
        #  is called in any AI-specific function, to prevent accidental cheating
        if restrict is None or self._player == restrict:
            return self._type
        else:
            return None

    def getPlayer(self):
        return self._player

    def getName(self):
        names = {"1": "Marshall",
                 "2": "General",
                 "3": "Colonel",
                 "4": "Major",
                 "5": "Captain",
                 "6": "Lieutenant",
                 "7": "Sergeant",
                 "8": "Miner",
                 "9": "Scout",
                 "S": "Spy",
                 "F": "Flag",
                 "B": "Bomb"}
        return names[self._type]

    def canMove(self):
        return self._type != "B" and self._type != "F"

    def beats(self, other):
        otherType = other.getType()
        if otherType == 'F':
            return True
        if otherType == 'B':
            return self._type == '8'
        if otherType == 'S' and self._type == "1":
            return False
        if otherType == "1" and self._type == 'S':
            return True
        if self._type == 'B':
            return otherType != '8'
        if self._type == 'F':
            return False
        types = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S']
        # In case that ranks are equal, returns False, because it doesn't beat the opponent
        #  in the game, that means both are removed, which is logic implemented in game, not here
        return types.index(self._type) < types.index(otherType)