from utils import randbool

class clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[(99 if(j==0 or i == 0 or j == h-1 or i == w-1 ) else 0)  for i in range(w)] for j in range(h)]
        self.update()

    def update(self, r = 1, mxr = 20, d = 1, mxd = 10):
        for i in range(self.h):
            for j in range(self.w):
                if(self.cells[i][j] == 99):
                    continue
                else:
                    if randbool(r,mxr):
                        self.cells[i][j] = 1
                        if randbool(d, mxd):
                            self.cells[i][j] = 2
                    else:
                        self.cells[i][j] = 0