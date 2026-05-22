# THIS FILE CREATES A ABSTRACT BASE OBJECT CLASS
# IT'S USED TO CREATE ALL GAME OBJECTS

from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x, y, symbol, color, name):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color
        self.name = name