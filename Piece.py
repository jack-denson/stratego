
class Piece:

    def __init__(self, type):
        assert(type in {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'F', 'B'})
        self._type = type

    def getType(self):
        return self._type

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
        return self._type != "Bomb" and self._type != "Flag"

    def beats(self, other):
        otherType = other.type
        if otherType == 'F':
            return True
        if otherType == 'B':
            return self._type == '8'
        if otherType == 'S' and self._type == "1":
            return False
        if otherType == "1" and self._type == 'S':
            return True
        types = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S']
        # In case that ranks are equal, returns False, because it doesn't beat the opponent
        #  in the game, that means both are removed, which is logic implemented in game, not here
        return types.index(self._type) < types.index(otherType)