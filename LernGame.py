#🌲🚁🌊🟩🔥🏥❤🧯☁⚡🌩🌪🌨🌋🏔🏚🏆🏬🔳
from Map import Map
import time
import os

TICK_SLEEP = 0.001
TREE_UPDATE = 100
FIRE_UPDATE = 200

m = Map(20,15)
m.generate_forest(2, 15)
m.generate_river(15)
m.generate_river(15)
m.add_fire()

tick = 1

stopTok = True

while  stopTok:
    os.system('cls')# unix = clear
    print(tick)
    m.print_map()
    tick +=1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fire()
