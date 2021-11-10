class Player:
    pass

class AI(Player):
    def __init__(self):
        pass

    def setPieces(self):
        # Long-term goal: get some logic in here for placing pieces in reasonable/strategic places
        # Realistic/short-term goal: place randomly, or semi-randomly(i.e. random, but knows to put flag in back)

    def observeMove(self, oldState, move, newState):
        # Watches opponent move, updates internal state to react to this

    def chooseMove(self, gameState):
        # Chooses a move for the agent

class Human(Player):
    def __init__(self):
        # Don't need much here, internal state stored in human's brain

    def setPieces(self):
        # Prompts user to set up pieces, or to select preset(e.g. 'random')

    def observeMove(self, oldState, move, newState):
        # Should be a no-op

    def chooseMove(self, gameState):
        # Prompts user for a move and waits
