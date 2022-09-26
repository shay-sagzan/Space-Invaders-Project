import curses
from utilities import Utilities

class Spaceship(Utilities):
    # Initial Variables
    shape = "=^="
    shotDir = -1
    bullet = 'Ʌ'
    shootWaitMaxTime = 5
    shootWaitTime = shootWaitMaxTime
    waitingShots = 0

    def __init__(self, stdscr: curses.window):
        """The function initiate the space-ship of the game"""
        super().__init__(stdscr)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        BLUE_AND_BLACK = curses.color_pair(2)
        self.pos = [self.height-5, self.width//2]
        self.isAlien = False
        self.color = BLUE_AND_BLACK


    def print(self):
        self.shootWaitTime = max(self.shootWaitTime-1, 0)
        if self.waitingShots > 0:
            self.shoot()
            self.waitingShots -= 1
        return super().print()

    def shoot(self):
        if self.shootWaitTime == 0:
            super().shoot()
            self.shootWaitTime = self.shootWaitMaxTime
            return
        self.waitingShots += 1

    def moveLeft(self):
        if 10 < self.pos[1]:
            self.pos[1] -= 1

    def moveRight(self):
        if self.pos[1] < self.width-2:
            self.pos[1] += 1

