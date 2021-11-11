
class Move:

    def __init__(self, r0, c0, r1, c1):
        self._r1 = r1
        self._c1 = c1
        self._r0 = r0
        self._c0 = c0

    def getStart(self):
        return self._r0, self._c0

    def getEnd(self):
        return self._r1, self._c1

    def toStr(self):
        return ("("+str(self._r0)+", "+str(self._c0)+") -> ("+str(self._r1)+", "+str(self._c1)+")")
