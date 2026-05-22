# THIS FILE GENERATES THE DUNGEON MAP 
# CONTAINS FREE SPACES, WALLS, ENEMIES, CHESTS, HIDDEN TRAPS
# AS WELL AS THE EXIT AND GRAYED OUT EXPLORED TERRAIN

import random

class DungeonMap:
    def __init__(self, width, height, level):
        self.width = width
        self.height = height
        self.level = level
        self.tiles = [[' ' for _ in range(width)] for _ in range(height)]
        self.explored = [[False for _ in range(width)] for _ in range(height)]
        self.enemies = []
        self.chests = []
        self.traps = []
        self.exit_pos = (0, 0)
        self.generate()

    def generate(self):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < 0.2:
                    self.tiles[y][x] = '#'
                else:
                    self.tiles[y][x] = '.'

        for x in range(self.width):
            self.tiles[0][x] = '#'
            self.tiles[self.height-1][x] = '#'
        for y in range(self.height):
            self.tiles[y][0] = '#'
            self.tiles[y][self.width-1] = '#'

        if self.level < 5:
            while True:
                ex, ey = random.randint(1, self.width-2), random.randint(1, self.height-2)
                if self.tiles[ey][ex] == '.':
                    self.exit_pos = (ex, ey)
                    self.tiles[ey][ex] = 'E'
                    break

    def is_blocked(self, x, y):
        return self.tiles[y][x] == '#'