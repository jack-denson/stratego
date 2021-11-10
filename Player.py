import util
import random

class Player:
    pass

class AI(Player):
    def __init__(self):
        pass

    def setPieces(self):
        # Long-term goal: get some logic in here for placing pieces in reasonable/strategic places
        # Realistic/short-term goal: place randomly, or semi-randomly(i.e. random, but knows to put flag in back)
        # Current behavior: completely random setup, nothing smart or strategic done at all
        pieces = util.startPieces(self)
        random.shuffle(pieces)
        return [pieces[0:10], pieces[10:20], pieces[20:30], pieces[30:40]]

    def observeMove(self, oldState, move, newState):
        return
        # Watches opponent move, updates internal state to react to this

    def chooseMove(self, gameState):

        return
        # Chooses a move for the agent

class Human(Player):
    def __init__(self):
        pass
        # Don't need much here, internal state stored in human's brain

    def setPieces(self):
        return
        # Prompts user to set up pieces, or to select preset(e.g. 'random')

    def observeMove(self, oldState, move, newState):
        return
        # Should be a no-op

    def chooseMove(self, gameState):
        return
        # Prompts user for a move and waits
