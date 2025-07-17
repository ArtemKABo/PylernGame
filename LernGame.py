#🌲🚁🌊🟩🔥🏥❤🧯☁⚡🌩🌪🌨🌋🏔🏚🏆🏬🔳

from pynput import keyboard
from Map import Map
import time
import os
from Helicopter import helicopter as helico
from Clouds import clouds

TICK_SLEEP = 0.001
TREE_UPDATE = 1000
FIRE_UPDATE = 2000
CLOUDS_UPDATE = 8000
MAP_H, MAP_W = 12 , 22


def game_over(helic):
    os.system('cls')
    print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")
    print(F"🔳GAME OVER. YOUR SCORE IS {helic.TotalScore}🔳")
    print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")

m = Map(MAP_W, MAP_H)

helic= helico(MAP_W, MAP_H)

def on_release(key):
    global stopTok
    if key.char.lower() == 'q':
        stopTok = False
    if key.char.lower() in "wasd":
        helic.move(key.char.lower())

stopTok = True

listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()

tick = 1

while  stopTok:
    os.system('cls')# unix = clear
    m.heli_procces(helic)
    if(helic.lives <= 0):
        stopTok = False
        continue
    helic.print_stats()
    m.print_map(helic)
    #print(tick)
    tick +=1
    if(tick % TREE_UPDATE == 0):
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fire(helic)
    if tick % CLOUDS_UPDATE == 0:
        m.clouds.update()
    time.sleep(TICK_SLEEP)
else:
    game_over(helic)