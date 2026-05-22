# THIS FILE CREATES AN ENEMY OBJECT
# IF IT'S A BOSS, IT'S MARKED AS SUCH AND HAS EXTREME STATS
# ALSO EXPLAINS HOW ENEMIES TAKE TURNS AND MOVE TOWARDS PLAYER

import math
from src.entities.character import Character
from src.misc.colors import Colors

class Enemy(Character):
    def __init__(self, x, y, name, diff_mod, stats_data=None):
        _, base_hp, s_str, s_dex, xp_reward = stats_data
        
        hp = int(base_hp * diff_mod)
        stats = {'str': s_str, 'dex': s_dex, 'per': 5, 'vit': 2, 'int': 0}
        self.xp_reward = xp_reward
        color = Colors.RED

        if "Dragon (Boss)" in name:
            color = Colors.MAGENTA
            hp = int(1000 * diff_mod)
            stats['str'] = 20
            stats['dex'] = 10
            self.xp_reward = 1000
        
        super().__init__(x, y, name[0], color, name, hp, 0, stats)

    def take_turn(self, player, map_obj):
        dist = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        if dist < 6:
            dx = 1 if player.x > self.x else -1 if player.x < self.x else 0
            dy = 1 if player.y > self.y else -1 if player.y < self.y else 0
            
            if not map_obj.is_blocked(self.x + dx, self.y):
                self.x += dx
            elif not map_obj.is_blocked(self.x, self.y + dy):
                self.y += dy