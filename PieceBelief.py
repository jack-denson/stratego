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

    def total(self):
        sum = 0
        for i in self.belief:
            sum += self.belief[i]
        
        return sum
    
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
