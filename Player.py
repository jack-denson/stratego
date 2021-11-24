import util
import random
import Move
import BoardBelief

class Player:
    pass

class AI(Player):
    def __init__(self, name):
        self._name = name
        self._belief = None

    def setPieces(self):
        # Long-term goal: get some logic in here for placing pieces in reasonable/strategic places
        # Realistic/short-term goal: place randomly, or semi-randomly(i.e. random, but knows to put flag in back)
        # Current behavior: completely random setup, nothing smart or strategic done at all
        pieces = util.startPieces(self)
        random.shuffle(pieces)
        return [pieces[0:10], pieces[10:20], pieces[20:30], pieces[30:40]]

    def initState(self, state):
        #Called when state is intitialized
        self._belief = BoardBelief.BoardBelief(state, self)

    def observeMove(self, player, move, battleInfo):
        self._belief.observeMove(player, move, battleInfo)
        return
        # Watches opponent move, updates internal state to react to this
        # Should NOT access opponent's piece ranks

    def getName(self):
        return self._name

    def chooseMove(self, state):
        return util.randomMove(state)

    def isHuman(self):
        return False

class Human(Player):
    def __init__(self, name):
        self._name = name
        pass
        # Don't need much here, internal state stored in human's brain

    def getName(self):
        return self._name
    
    def initState(self, state):
        return

    def setPieces(self):
        # Prompts user to set up pieces, or to select preset(e.g. 'random')

        config = input("Input piece configuration(random, wikipedia, or custom as 40-char string): ")
        if config == "" or config == "random" or config == "rand" or config == "r":
            pieces = util.startPieces(self)
            random.shuffle(pieces)
            return [pieces[0:10], pieces[10:20], pieces[20:30], pieces[30:40]]
        elif config == "wikipedia" or config == "wiki" or config == "w":
            return util.wikipediaSetup(self)
        else:
            return util.setupFromString(self, config)

    def observeMove(self, move, battleInfo):
        return
        # Should be a no-op, player is observing move themselves

    def chooseMove(self, gameState):
        # Prompts user for a move and waits

        gameState.show()

        validMove = False

        while not validMove:
            validStart = False
            while not validStart:
                startPos = input("Enter coordinates of piece to move: ")
                validStart = util.validPos(startPos)
                if startPos.lower() == 'random':
                    return util.randomMove(gameState)
                if not validStart:
                    print("Invalid coordinates")

            startR, startC = util.toCoords(startPos)

            validEnd = False
            while not validEnd:
                endPos = input("Enter coordinates of location to move to: ")
                validEnd = util.validPos(startPos)
                if not validEnd:
                    print("Invalid coordinates")

            endR, endC = util.toCoords(endPos)

            move = Move.Move(startR, startC, endR, endC)
            validMove = gameState.isValid(move)

            if not validMove:
                print("Move is invalid. Try again")

        return move

    def isHuman(self):
        return True