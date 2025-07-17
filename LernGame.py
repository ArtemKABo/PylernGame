#🌲🚁🌊🟩🔥🏥❤🧯☁⚡🌩🌪🌨🌋🏔🏚🏆🏬🔳
from Map import Map
import time
import os
from Helicopter import helicopter as helico

TICK_SLEEP = 0.001
TREE_UPDATE = 100
FIRE_UPDATE = 200
MAP_H, MAP_W = 15 , 20

m = Map(MAP_W, MAP_H)
m.generate_forest(2, 15)
m.generate_river(15)
m.generate_river(15)
m.add_fire()

helic= helico(MAP_W//2, MAP_H//2 )

tick = 1

stopTok = True

while  stopTok:
    os.system('cls')# unix = clear
    print(tick)
    m.print_map(helic)
    tick +=1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fire()
