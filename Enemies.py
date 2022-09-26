import curses
from random import randrange, seed
from utilities import Utilities


class Enemy(Utilities):
    # Initial Variables
    shape = "X"
    bullet = 'V'
    shotDir = 1

    def __init__(self, stdscr: curses.window, col, row = 1):
        """The function initiate the enemies of the game"""
        seed(col)
        self.newShootTime()
        super().__init__(stdscr)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        RED_AND_BLACK = curses.color_pair(3)
        self.pos = [row + 2, col]
        self.isAlien = True
        self.color = RED_AND_BLACK

    def newShootTime(self):
        self.shoot_wait = randrange(100, 1000)

    def print(self):
        super().print()
        if self.shoot_wait == 0:
            self.shoot()
            self.newShootTime()
            return
        self.shoot_wait -= 1
