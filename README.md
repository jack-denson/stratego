# Stratego
Implementation by Jack Denson

Stratego game with AI agent
Created for CS4100 - Artificial Intelligence final project

To play: `python Game.py`

By default, plays one game, human player against random agent. In the future, I will add command line arguments
to make it easier to play player vs. player, ai vs. ai, multiple games, and to change game settings.

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