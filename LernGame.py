#🌲🚁🌊🟩🔥🏥❤🧯☁⚡🌩🌪🌨🌋🏔🏚🏆🏬🔳

from pynput import keyboard
from Map import Map
import time
import json
import os
from Helicopter import helicopter as helico
from Clouds import clouds

TICK_SLEEP = 0.001
TREE_UPDATE = 900
FIRE_UPDATE = 1100
CLOUDS_UPDATE = 3900
MAP_H, MAP_W = 12 , 22


def game_over(helic):
    os.system('cls')
    print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")
    print(F"🔳 GAME OVER. YOUR SCORE IS {helic.TotalScore}🔳")
    print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")


m = Map(MAP_W, MAP_H)

helic= helico(MAP_W, MAP_H)

def load_game():
    global helic, m
    with open("level.json", "r") as lvl:
        data = json.load(lvl)
        helic.import_data(data["helcopter"]) 
        m.import_map(data["Map"])

def on_release(key):
    global stopTok
    #При пекрехвате перехватывает всякое и это не всегда символы
    try:
        c = key.char.lower()
        if c == 'q':
            stopTok = False
        if c in "wasd":
            helic.move(key.char.lower())
        if c == "f":
            data = {"helcopter": helic.export_data(),
                    "Map": m.export_data()}
            with open("level.json", "w") as lvl:
                json.dump(data, lvl)
        if c == "g":
           load_game()
    except Exception as e:
        print(e)
        None

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