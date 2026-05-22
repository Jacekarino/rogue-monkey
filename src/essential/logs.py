# THIS FILE HANDLES THE GAME LOG THAT DISPLAYS WHAT HAPPENS IN THE GAME
# THE MESSAGES THEMSELVES ARE STORED IN VARIOUS OTHER FILES

from src.misc.colors import Colors

class GameOver(Exception):
    pass

class GameLog:
    def __init__(self):
        self.messages = []

    def add(self, message):
        self.messages.append(message)
        if len(self.messages) > 10:
            self.messages.pop(0)

    def display(self):
        print(f"<<< LOG >>>")
        for msg in self.messages:
            print(f"> {msg}")

game_log = GameLog()