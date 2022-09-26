import curses

from utilities import Utilities

class Defense(Utilities):
    # Initial Variables
    shape = "###"
    row_start = 1
    row_end = 45
    
    def __init__(self, stdscr: curses.window):
        """The function initiate the defense of the space-ship"""
        super().__init__(stdscr)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        GREEN_AND_BLACK = curses.color_pair(1)
        self.pos = [self.height - 20, self.width//2]
        self.isAlien = False
        for i in range(self.row_start):
            for j in range(0, self.row_end, 1):
                if j == 1 or j == 10 or j == 20 or j == 30 or j == 40:
                    stdscr.addstr(i + 20, j + 30, self.shape, GREEN_AND_BLACK)



