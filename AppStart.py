
from pynput import keyboard
from Game import Game

game = Game()

listener = keyboard.Listener(
    on_press=None,
    on_release= game.on_release)
listener.start()

game.start_game()