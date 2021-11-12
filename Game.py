import GameState as gs
import Player
import util

def playGame(p0, p1, spectate):
    # If spectate is on, show board for all player's turns
    # If spectate is off, show board for Human players, don't show board for AIs
    # This is where we include game-over logic, etc
    # BattleInfo for each nextState transition should include info for whether flag was captured
    # User input should be handled in Player.py

    winner = None
    state = gs.GameState(players=[p0, p1])
    while winner is None:
        if(spectate):
            # If we're watching this game, print it out. If there are more than 0 human players, it will be printed
            #  out automatically by the select move logic
            state.show(spectate)

        playerToMove = state.currentPlayer()
        move = playerToMove.chooseMove(state)

        print(playerToMove.getName()+" moves from "+util.toUserCoord(*move.getStart())
              + " to " + util.toUserCoord(*move.getEnd()))

        state, battleInfo = state.nextState(move)
        if len(battleInfo) > 0:
            print(battleInfo[0] + " attacks " + battleInfo[1])
            if battleInfo[1] == "F":
                winner = playerToMove

    print("Game Over!")

playGame(Player.Human("Player"), Player.AI("AI"), False)
"""
if i % 2 == 0:
    state.show(False)
moves = state.getValidMoves()
move = random.choice(moves)
state, battleInfo = state.nextState(move)
if len(battleInfo) > 0:
    print(battleInfo[0] + " attacks " + battleInfo[1])
print(move.toStr())"""