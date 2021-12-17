# Stratego
Implementation by Jack Denson

Stratego game with AI agent
Created for CS4100 - Artificial Intelligence final project

To play: `python Stratego.py`

By default, plays one game, human player against random agent.

The following are all optional command line arguments:
```
  -h, --help            show this help message and exit
  -n NUM_GAMES, --num-games NUM_GAMES
                        The number of games to play
  -a, --ai              Whether to play 2 AIs against each other(instead of default play against AI)
  -s, --spectate        Whether to watch(print out board) during play between AIs
  -p NAME, --name NAME  Set the name of Player(default 'User')
  -q, --quiet           Only output result of games, not moves
  -b, --belief          See belief of AI(useful for debugging)
  -c, --colorless       Deactivate colored terminal(for terminals that don't support color codes)
  -e EVALS EVALS, --evals EVALS EVALS
                        Evaluation function for AI agents(only works when -a flag is also used)
```

The evaluation functions are as follows - not all of them are fully tested out:
```
numEnemies: by number of enemy pieces
null | none | nullEval: always return 0(choose random move)
flags | numFlags: eval by number of expected flags
fnb | flagsAndBombs: eval by number of expected flags, plus number expected bombs
targetBombs | bombs: eval by how close miners are to enemy bombs, plus number of each of those piece types
forward | fwd | justMoveForward: eval by piece y location(for some reason, only works for blue, not red)
```
## Setup

When the game starts, it is necessary to place all 40 game pieces in any configuration on the game board.
A human player is prompted to do so, but to speed up this process, a few presets are built-in.

 - `random`, `rand`, `r`, or no input places pieces randomly
 - `wikipedia`, `wiki`, or `w` places pieces in the configuration shown [here](https://en.wikipedia.org/wiki/Stratego#/media/File:Stratego.png), the wikipedia page for Stratego.
   This is a reasonably strategic configuration
 - `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`, where `X` is any piece code, places the pieces in that order, top row to bottom row.

Currently, AI players do not have any way of placing their pieces non-randomly(i.e. with any sort of strategy). This is a stretch goal for this project, and is what I intend to tackle if I am
happy with the ability of the agent to move given an already-defined state.
## Gameplay

The game runs in the terminal, asking for the coordinate of the piece to move, then the coordinate of the place
to move this piece to.

Pieces can move based on rules described [here](https://en.wikipedia.org/wiki/Stratego), and capture each other based on
rules also described there.

AI agent will move randomly, which will change very soon. Behavior of AI agents is located in [Player.py](Player.py)