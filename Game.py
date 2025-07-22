#🌲🚁🌊🟩🔥🏥❤🧯☁⚡🌩🌪🌨🌋🏔🏚🏆🏬🔳
# Переделать механику огня
from pynput import keyboard
from Map import Map
import time
import json
import os
from sys import platform
from Helicopter import helicopter as helico

class Game:

    __TICK_SLEEP = 0.0016
    os_command = "clear"
    tick = 1

    tree_UPDATE = 1200
    fire_UPDATE = 1200
    clouds_UPDATE = 2500
    cloud_COWER = 1 
    thunder_COWER = 1
    stopTok = True

    def __init__(self, w = 10, h = 10):
        self.h = h
        self.w = w
        self.map = Map(w, h)
        self.helico = helico(w, h)
        self.__difining_platform()

    def __Menu(self):
        os.system(self.os_command)
        print(" 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n",
              "🟩🟩🟩      ПОЖАРНЫЙ ВЕРТОЛЕТ     🟩🟩🟩\n", 
              "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n",
              "Введите q чтобы выйти или закончить мгру \n",
              "Введите 1 чтобы создать новую игру \n",
              "Ввудите 2 чтоб продолжить игру с сохраненного места \n")
        r = input("🔥🔥🔥🔥🔥 : ")
        if r == "1":
            self.__Create_Game()
        elif r == "2":
            self.__start_Load_game()
        elif r == "q":
            None
        else:
            self.__Menu()

    def __difining_platform(self):
        if platform == "linux" or platform == "linux2":
            self.os_command =  "clear"
        elif platform == "darwin":
            self.os_command =  "clear"
        elif platform == "win32":
            self.os_command =  "cls"
        else:
            self.os_command =  "clear"

    def __Create_Game(self):
        os.system(self.os_command)
        self.h = self.__inputIntOrReinput("Введите высоту игрвого поля : ")
        self.w = self.__inputIntOrReinput("Введите ширину игрового поля : ")
        f = self.__inputIntOrReinput("Интенсивность возникновения новых пожаров : ") 
        self.cloud_COWER = (self.__inputIntOrReinput("Введите интенсивность облачности : ")) % 20
        self.thunder_COWER = (self.__inputIntOrReinput("Bведите интенсивность гроз : ")) % 10
        d = self.__inputIntOrReinput("Введите множитель сложности : ")
        self.map.generat_map(self.w, self.h, f, d)
        self.helico = helico(self.w, self.h)
        self.__engin_game()

    def __inputIntOrReinput(self, text):
        try:
            return int(input(text))
        except:
            print("Произошол некоректный ввод попробуйте сного")
            return self.__inputIntOrReinput(text)

    def __game_over(self):
        os.system(self.os_command)
        print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")
        print(F"🔳 GAME OVER. YOUR SCORE IS {self.helico.TotalScore}🔳")
        print("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳")
        y = input("Ввудите y если хотите загрузить предыдущее сохранение: ")
        if y == 'y':
            self.__start_Load_game()
        else:
            self.__Menu()

    def __start_Load_game(self):
            self.__load_game()
            self.__engin_game()

    def __save_game(self):
            data = { "h": self.h,
                    "w": self.w,
                    "cc": self.cloud_COWER,
                    "tc": self.thunder_COWER,
                    "helcopter": self.helico.export_data(),
                    "Map": self.map.export_data()}
            with open("level.json", "w") as lvl:
                json.dump(data, lvl)
         
    def __load_game(self):
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            self.h = data["h"] or 10
            self.w = data["w"] or 10
            self.cloud_COWER = data["cc"] or 1
            self.thunder_COWER = data["tc"] or 1
            self.map = Map(self.w, self.h)
            self.helico = helico(self.w, self.h)
            self.helico.import_data(data["helcopter"]) 
            self.map.import_map(data["Map"])

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
                self.__save_game()
            if c == "g":
                self.__load_game()
        except :#Exception as e:
            #print(e)
            None

    def start_game(self):
        self.__Menu()

    def __engin_game(self):
        self.stopTok = True
        while  self.stopTok:
            os.system(self.os_command)
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
                self.map.clouds.update( self.cloud_COWER, 20, self.thunder_COWER, 20)
            if self.tick == 20000:
                self.tick = 1
            time.sleep(self.__TICK_SLEEP)
        else:
            self.__game_over()



