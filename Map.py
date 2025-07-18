#💖🧯🏆
# 0 = 🔳
# 1 = 🟩
# 2 = 🌲
# 3 = 🌊
# 4 = 🏥
# 5 = 🏬
# 6 = 🗻
# 7 = 🔥
# 8 = 🚁
# 9 = ☁
# 10 = ⚡
from utils import randbool as rb
from utils import randcell
from utils import randcell2
from utils import randboardcell as startRiver
from Clouds import clouds

CELL_TYPES = "🔳🟩🌲🌊🏥🏬🗻🔥🚁"

class Map:
                 
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.upcost = 5000
        self.lifecost = 10000
        self.firestraff = 200
        self.clouds = clouds(w,h)
        self.cells = [[(0 if(j==0 or i == 0 or j == h-1 or i == w-1 ) else 1)  for i in range(w)] for j in range(h)]
        self.generate_forest(2, 15)
        self.generate_river(15)
        self.generate_river(15)
        self.generate_upgrade_centre()
        self.generate_hospiral()
        self.add_fire()

    def check_baunds(self, w, h):
        if ( h < 0 or w < 0 or  w >= self.w or h >= self.h or self.cells[h][w] == 0):
            return False
        return True
    
    def print_map(self, helic):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if(self.clouds.cells[ri][ci] == 1):
                    print('☁️.', end="")#
                elif(self.clouds.cells[ri][ci] == 2):
                    print('⚡️', end="")    
                elif(helic.x == ci and helic.y == ri):
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
    
    def update_fire(self, helico):
        for ri in range(self.h) :
            for ci in range(self.w):
                if self.cells[ri][ci] == 7:
                    self.cells[ri][ci] = 1
                    helico.score -= self.firestraff
                    helico.TotalScore -= self.firestraff
                    self.add_fire()
        if rb(2,3):
            self.add_fire()

    def generate_upgrade_centre(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if(self.check_baunds(cx,cy) and self.cells[cy][cx] != 3 and self.cells[cy][cx] != 4):
            self.cells[cy][cx] = 5
        else:
            self.generate_upgrade_centre()

    def generate_hospiral(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if(self.check_baunds(cx,cy) and self.cells[cy][cx] != 3 and self.cells[cy][cx] != 5):
            self.cells[cy][cx] = 4
        else:
            self.generate_hospiral()

    def heli_procces(self, helico):
        c = self.cells[helico.y][helico.x]
        d = self.clouds.cells[helico.y][helico.x]
        if(c == 3):
            helico.tank = helico.mxtank
        if(c == 7 and helico.tank > 0):
            helico.tank -= 1
            helico.score += 100
            helico.TotalScore += 100
            self.cells[helico.y][helico.x] = 2
        if(c == 5 and helico.score >= self.upcost):
            helico.score -= self.upcost
            helico.mxtank += 1
            if(helico.mxtank % 4 == 0):
                helico.mxlife += 1
        if(c == 4 and helico.score >= self.lifecost and helico.lives < helico.mxlife):
            helico.score -= self.lifecost
            helico.lives += 100
        if(d == 2):
            helico.lives -= 1
   
    def export_data(self):
        return {"cells" : self.cells,
                "clouds": self.clouds.cells}
    
    def import_map(self, data):
        self.cells = data["cells"] or self.cells
        self.clouds.cells = data["clouds"] or self.clouds.cells

