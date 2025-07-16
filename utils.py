from random import randint as rand

def randbool(r, xmr):
    t = rand(0, xmr)
    return (t<=r)

def randcell(w, h):
    tw = rand(1, w-2)
    th = rand(1, h-2)
    return(tw,th)

def randboardcell(w, h):
    l1 = (w-2)
    l2 = (h-2)
    c = rand(0, (l1 + l2)*2)
    if(c <= l1):
        return(c+1, 1)
    elif(c <= l1+l2):
        return(w-2, c-l1+1)
    elif(c <= l1*2 + l2):
        return((l1*2 + l2) - c+1, h-2 )
    else: 
        return(1, (l1 + l2)*2 - c)


#0 - наверх, 1 - направо, 2 - вниз, 3 - направо
def randcell2(x, y):
    moves = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)