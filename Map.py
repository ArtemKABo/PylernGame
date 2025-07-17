#💖🧯☁⚡🌩🌪🌨🏆
# 0 = 🔳
# 1 = 🟩
# 2 = 🌲
# 3 = 🌊
# 4 = 🏥
# 5 = 🏬
# 6 = 🗻
# 7 = 🔥
# 8 = 🚁
from utils import randbool as rb
from utils import randcell
from utils import randcell2
from utils import randboardcell as startRiver

CELL_TYPES = "🔳🟩🌲🌊🏥🏬🗻🔥🚁"

class Map:
                 
    def __init__(self, w, h ):
        self.w = w
        self.h = h
        self.cells = [[(0 if(j==0 or i == 0 or j == h-1 or i == w-1 ) else 1)  for i in range(w)] for j in range(h)]

    def check_baunds(self, w, h):
        if ( h < 1 or w < 1 or  w >= self.w-1 or h >= self.h-1 or self.cells[h][w] == 0):
            return False
        return True
    
    def print_map(self, helic):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if(helic.x == ri and helic.y == ci):
                    print(CELL_TYPES[8], end="")
                elif(cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print()


    #надо переделать
    def generate_river(self, l):
        rc = startRiver(self.w, self.h) if rb(1,3) else  randcell(self.w, self.h) #
        rx, ry = rc[0], rc[1]
        self.cells[ry][rx] = 3
        while l > 0:
            rc2 = randcell2(rx,ry)
            rx2, ry2 = rc2[0], rc2[1]
            if(self.check_baunds(rx2, ry2) ):

                self.cells[ry2][rx2] = 3
                rx, ry = rx2, ry2
                l -= 1

    def WaterColisium(self, x, y):
        pass

    def isWater(self, x, y):
        return self.cells[y][x] == 3

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if(self.cells[ri][ci] == 0):
                    continue
                if rb(r, mxr):
                    self.cells[ri][ci] = 2

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if(self.check_baunds(cx,cy) and self.cells[cy][cx] == 1):
            self.cells[cy][cx] = 2

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if(self.check_baunds(cx,cy) and self.cells[cy][cx] == 2):
            self.cells[cy][cx] = 7
        else:
            self.add_fire()
    
    def update_fire(self):
        for ri in range(self.h) :
            for ci in range(self.w):
                if self.cells[ri][ci] == 7:
                    self.cells[ri][ci] = 1
                    self.add_fire()
   