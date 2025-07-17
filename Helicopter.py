from utils import moves
from utils import randcell

class helicopter:
    def __init__(self, w, h):
        rc = randcell(w,h)
        self.w = w
        self.h = h
        self.x = rc[0]
        self.y = rc[1]
        self.tank = 0
        self.mxtank = 1
        self.mxlife = 200
        self.lives = self.mxlife
        self.score = 0
        self.TotalScore = 0

    def move(self, c):
        rc = moves(c)
        nx, ny = rc[0] + self.x, rc[1] + self.y
        if(nx > 0 and ny > 0  and nx < self.w -1 and ny < self.h-1):
            self.x, self.y = nx, ny 

    def print_stats(self):
        print('🧯' , self.tank, '/',self.mxtank, "    ", '💖', self.lives,'/', self.mxlife, "    ", "🏆", self.score, sep="" )