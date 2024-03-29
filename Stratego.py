import argparse
import Player
import Game
import Evaluators

parser = argparse.ArgumentParser(description='Play any number of Stratego games with an AI')
parser.add_argument('-n', '--num-games', type=int, nargs=1, default=[1], help="The number of games to play")
parser.add_argument('-a', '--ai', action='store_true', help='Whether to play 2 AIs against each other(instead of default play against AI)')
parser.add_argument('-s', '--spectate', action='store_true', help='Whether to watch(print out board) during play between AIs')
parser.add_argument('-p', '--name', default="User", help='Set the name of Player(default \'User\')')
parser.add_argument('-q', '--quiet', action='store_true', help='Only output result of games, not moves')
parser.add_argument('-b', '--belief', action='store_true', help='See belief of AI(useful for debugging)')
parser.add_argument('-c', '--colorless', action='store_true', help='Deactivate colored terminal(for terminals that don\'t support color codes)')
parser.add_argument('-e', '--evals', nargs=2, default=[None, None], help='Evaluation function for AI agents')

#To test that minimax makes a difference, we need options for evaluators

args = parser.parse_args()
p1Wins = 0
p2Wins = 0

for i in range(args.num_games[0]):
    p1 = Player.AI("AI Player 1", evaluator=Evaluators.evalMap[args.evals[0]])
    if args.ai:
        p2 = Player.AI("AI Player 2", evaluator=Evaluators.evalMap[args.evals[1]])
    else:
        p2 = Player.Human(args.name)

    winner = Game.playGame(p1, p2, args.spectate, quiet=args.quiet, seeBelief=args.belief, color=(not args.colorless))

    if winner == p1.getName():
        p1Wins += 1
    else:
        p2Wins += 1

print("\n\n")
print("Game" + ("s" if args.num_games[0] > 1 else "") + " over")
print(p1.getName() +" won " + str(p1Wins) + " game" + ("s" if p1Wins != 1 else "") + " (" + (str(100*p1Wins/args.num_games[0])[:5]) + "%)")
print(p2.getName() +" won " + str(p2Wins) + " game" + ("s" if p2Wins != 1 else "") + " (" + (str(100*p2Wins/args.num_games[0])[:5]) + "%)")
