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
from random import randint

CELL_TYPES = "🔳🟩🌲🌊🏥🏬🗻🔥🚁"

class Map:
                 
    def __init__(self, w, h, f = 1, d = 2 ):
        self.w = w
        self.h = h
        self.Fire = f
        self.difficulte = d
        self.upcost = 500 * d
        self.lifecost = 1000 *d
        self.firestraff = 100 * d
        self.clouds = clouds(w,h)
        self.cells = [[(0 if(j==0 or i == 0 or j == h-1 or i == w-1 ) else 1)  for i in range(w)] for j in range(h)]
        self.generate_forest(3, 20)
        #self.generate_river(15) #w, h, d)
        #self.generate_river(15) 
        self.__generate_waters()
        self.generate_upgrade_centre()
        self.generate_hospiral()
        self.__create_all_Fire()

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

    def __generate_waters(self):
        ind= (self.w*self.h)//150
        if ind == 0: ind = 1
        for i in range(ind):
            self.__generate_river() if rb(1,2) else self.__Generate_Lake()

    def __Generate_Lake(self):
        lake = []
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[ry][rx] = 3
        lake.append([ry, rx]) 
        l = (randint(5,30) // self.difficulte) + 1
        while len(lake) <= l:
            for i in lake:
                if len(lake) >= l : 
                    break
                lake.extend( self.__update_lake( i[0], i[1]) )
                
    def __update_lake(self, y, x):
        lake = []
        if rb(1,2):
            lake.append(self.__newWater(y + 1, x)) 
        if rb(1,2):
            lake.append(self.__newWater(y - 1, x) ) 
        if rb(1,2):
            lake.append(self.__newWater(y, x + 1) ) 
        if rb(1,2):
            lake.append(self.__newWater(y, x- 1) ) 
        return lake

    def __newWater(self, y, x):
        if(self.check_baunds(x, y)):
            if (self.cells[y][x] == 3):
                return
            if rb(1,2):
                self.cells[y][x] = 3
                return [y, x]

    def __generate_river(self):
        rc = startRiver(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[ry][rx] = 3
        l = (randint(5,30)// self.difficulte) + 1
        while l > 0:
            rc2 = randcell2(rx,ry)
            rx2, ry2 = rc2[0], rc2[1]
            if(self.check_baunds(rx2, ry2) ):
                #if self.cells[ry2][rx2] == 3:
                    #rh = self.__WaterColisium(rx, ry, ry2, rx2)
                    #self.cells[rh[1]][rh[0]] = 3
                    #rx, ry = rh[0], rh[1]
                #else:
                self.cells[ry2][rx2] = 3
                rx, ry = rx2, ry2
                l -= 1

    def __WaterColisium(self, ox, oy, x, y):
        if ox > x:
            if(self.check_baunds(x - 1, y) ):
                if self.cells[y][x - 1] == 3:
                    return self.__WaterColisium(x, y, x - 1, y)
                else:
                    return [x-1, y]
            else:
                return self.__WaterColisium(x, y, x, y - 1)
        if ox < x:
            if(self.check_baunds(x + 1, y) ):
                if self.cells[y][x + 1] == 3:
                    return self.__WaterColisium(x, y, x + 1, y)
                else:
                    return [x+1, y]
            else:
                return self.__WaterColisium(x, y, x, y + 1)

        if oy > y:
            if(self.check_baunds(x , y - 1) ):
                if self.cells[y - 1][x] == 3:
                    return self.__WaterColisium(x, y, x , y - 1)
                else:
                    return [x, y - 1]
            else:
                return self.__WaterColisium(x, y, x + 1, y )

        if oy < y:
            if(self.check_baunds(x , y + 1) ):
                if self.cells[y + 1][x] == 3:
                    return self.__WaterColisium(x, y, x, y + 1)
                else:
                    return [x, y + 1]
            else:
                return self.__WaterColisium(x, y, x - 1, y )


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

    def __create_all_Fire(self):
        for i in range(self.Fire):
            if rb(1,2):
                self.__add_fire()
    
    def __add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if(self.check_baunds(cx,cy) and self.cells[cy][cx] == 2):
            self.cells[cy][cx] = 7
        else:
            self.__add_fire()

    def __spreading_the_flame(self, y, x):
        if rb(1,2):
            self.__newFire(x + 1, y) 
        if rb(1,2):
            self.__newFire(x - 1, y) 
        if rb(1,2):
            self.__newFire(x, y + 1) 
        if rb(1,2):
            self.__newFire(x, y - 1)
          
    def __newFire(self, x, y):
        if(self.check_baunds(x, y) and self.cells[y][x] == 2 ):
            self.cells[y][x] = 7

    def update_fire(self, helico):
        for ri in range(self.h) :
            for ci in range(self.w):
                if self.cells[ri][ci] == 7:
                    self.cells[ri][ci] = 1
                    helico.score -= self.firestraff
                    helico.TotalScore -= self.firestraff
                    self.__spreading_the_flame(ri, ci)
        self.__create_all_Fire()

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
        return {"fi": self.Fire,
                "di" : self.difficulte,
                "cells" : self.cells,
                "clouds": self.clouds.cells}
    
    def import_map(self, data):
        self.Fire = data["fi"] or 1
        self.difficulte = data["di"] or 2
        self.cells = data["cells"] or self.cells
        self.clouds.cells = data["clouds"] or self.clouds.cells

