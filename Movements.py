from curses import window
from os import minor
# from typing import List
from Enemies import Enemy
from Board import Board


class Movements:
    # Initial Variables
    invaderTimeToMove = 9
    moveCountDown = invaderTimeToMove
    moveDir = 1
    invaders = []

    def __init__(self, stdscr: window, invaders_col: int, invaders_row: int):
        """The function initiate the movements of entities in the game"""
        self.width = stdscr.getmaxyx()[1]
        center = self.width//2
        for i in range(invaders_row):
            for j in range(invaders_col):
                self.invaders.append(Enemy(stdscr,
                                             center+j-(invaders_col), i+1))

    def print(self):
        self.moveCountDown -= 1
        for i in self.invaders:
            if i.isDead:
                self.invaders.remove(i)
                Board.score += 1
                del i
                continue
            if self.moveCountDown == 0:
                if self.moveDir == 1:
                    i.pos[1] += 1
                else: i.pos[1] -= 1
            if not self.clearBellow(i):
                i.shoot_wait = -1
            elif i.shoot_wait < 0:
                i.newShootTime()
            i.print()
        if self.moveCountDown == 0:
            self.moveCountDown = self.invaderTimeToMove
        if not (20 < self.checkForEdgeInvader(min).pos[1] and self.checkForEdgeInvader(max).pos[1] < self.width-20):
            self.moveDir *= -1
            for i in self.invaders:
                i.pos[0] += 1
       
    def checkForEdgeInvader(self, minOrMax):
        return minOrMax(self.invaders, key=lambda x: x.pos[1] if not x.isDead else 999999)

    def clearBellow(self, invader):
        for i in self.invaders:
            if i.pos[0] < invader.pos[0]:
                return False
        return True
