#🌲🚁🌊🟩🔥🏥❤🧯☁⚡🌩🌪🌨🌋🏔🏚🏆🏬🔳
#todo Переименовать текущий файл
# Создать меню выбор сложности игры, размера карты, загрузка сохраненной игры
# Переделать механику огня
from pynput import keyboard
from Map import Map
import time
import json
import os
from Helicopter import helicopter as helico

class Game:

    __TICK_SLEEP = 0.001
    tick = 1

    tree_UPDATE = 900
    fire_UPDATE = 1100
    clouds_UPDATE = 3900
    stopTok = True

    def __init__(self, w = 10, h = 10, d=0):
        self.h = h
        self.w = w
        #self.CreateDificult(d)
        self.map = Map(w, h)
        self.helico = helico(w, h)

    def Menu(self):
        input("")

    def game_over(self):
        os.system('cls')
        print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")
        print(F"🔳 GAME OVER. YOUR SCORE IS {self.helico.TotalScore}🔳")
        print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")


    def load_game(self):
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            self.helico.import_data(data["helcopter"]) 
            m.import_map(data["Map"])

    def on_release(self, key):
        global stopTok
        #При пекрехвате перехватывает всякое и это не всегда символы
        try:
            c = key.char.lower()
            if c == 'q':
                self.stopTok = False
            if c in "wasd":
                self.helico.move(key.char.lower())
            if c == "f":
                data = {"helcopter": self.helico.export_data(),
                        "Map": m.export_data()}
                with open("level.json", "w") as lvl:
                    json.dump(data, lvl)
            if c == "g":
                self.load_game()
        except :#Exception as e:
            #print(e)
            None

    def start_game(self):
        self.stopTok = True
        while  self.stopTok:
            os.system('cls')# unix = clear
            self.map.heli_procces(self.helico)
            if(self.helico.lives <= 0):
                self.stopTok = False
                continue
            self.helico.print_stats()
            self.map.print_map(self.helico)
            #print(tick)
            self.tick +=1
            if(self.tick % self.tree_UPDATE == 0):
                self.map.generate_tree()
            if self.tick % self.fire_UPDATE == 0:
                self.map.update_fire(self.helico)
            if self.tick % self.clouds_UPDATE == 0:
                self.map.clouds.update()
            time.sleep(self.__TICK_SLEEP)
        else:
            self.game_over()



