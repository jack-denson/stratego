import util
import random
# A belief distribution for a single piece

class PieceBelief:

    def __init__(self):
        self.belief = {
            '1': 1/40,
            '2': 1/40,
            '3': 2/40,
            '4': 3/40,
            '5': 4/40,
            '6': 4/40,
            '7': 4/40,
            '8': 5/40,
            '9': 8/40,
            'S': 1/40,
            'F': 1/40,
            'B': 6/40}
    
    def certain(self, piece):
        # Only to be called when we are certain of something, e.g., we battle a piece and find out what it is
        for type in self.belief:
            self.belief[type] = 0
        
        self.belief[piece] = 1
    
    def isCertain(self):
        self.normalize()
        for i in self.belief:
            if self.belief[i] == 1:
                return self.total() == 1

    def total(self):
        sum = 0
        for i in self.belief:
            sum += self.belief[i]
        
        return sum
    
    def mostLikely(self):
        likely = '1'
        for i in self.belief:
            if self.belief[i] > self.belief[likely]:
                likely = i
        
        return likely

    def sample(self):
        running = 0
        rand = random.random() * self.total()
        for i in self.belief:
            running += self.belief[i]
            if running >= rand:
                return i
    
    def normalize(self):
        oldSum = self.total()
        for i in self.belief:
            self.belief[i] = self.belief[i] / oldSum
    
    def eliminatePossibility(self, type):
        assert type in self.belief
        self.belief[type] = 0
        self.normalize()

    def movable(self):
        self.eliminatePossibility("B")
        self.eliminatePossibility("F")

    def updateFromRemaining(self, pieceDist):
        sum = 0
        for i in pieceDist:
            sum += pieceDist[i]
        
        for i in pieceDist:
            self.belief[i] *= pieceDist[i]/sum

        self.normalize()

    def updateProbFromCert(self, remainingDist, certPiece):
        # Called when we find a DIFFERENT piece(not this one) that is DEFINITELY = certPiece
        # We would know this if it is a 9 that moves more than 1 space, or if we battle it
        # Uses P(P1=X | P2 = Y) = P(p2 = Y | p1= X) * P(p1 = X) to calculate this(Bayesian stats)
        # Remainingdist is all the pieces that we are unsure about(which must account for this one)
        assert not self.isCertain()

        for poss in self.belief:
            remainingIfEq = remainingDist.copy()
            remainingIfEq[poss] = remainingIfEq[poss] - 1
            self.belief[poss] = (remainingIfEq[certPiece] / util.sumOfDist(remainingIfEq)) * self.belief[poss]
        
        self.normalize()
