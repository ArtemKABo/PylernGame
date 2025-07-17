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

def moves(a):
    moves = { 'w':[0, -1], 'd':[1, 0], 's':[0, 1], 'a':[-1, 0]}
    if a in moves.keys():
        return moves[a]
    return[0, 0]

#0 - наверх, 1 - направо, 2 - вниз, 3 - направо
def randcell2(x, y):
    move = ['w', 'a', 's', 'd']
    t = rand(0, 3)
    rc = moves(move[t])
    return (x + rc[0], y + rc[1])