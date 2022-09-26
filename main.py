import curses
from utilities import Utilities
from Movements import Movements
from hitsManager import HitsManager
from Spaceship import Spaceship
from Defense import Defense
from Board import Board
from time import sleep


def main(stdscr: curses.window):
    # initial settings
    curses.curs_set(0)
    stdscr.nodelay(True)

    # Initialization
    board = Board(stdscr)
    defense = Defense(stdscr)
    hitsManager = HitsManager()
    Utilities.setHitsManager(hitsManager)
    spaceship = Spaceship(stdscr)
    enemies = Movements(stdscr, 11, 5)
    hitsManager.addEntity(defense)
    hitsManager.addEntity(spaceship)
    hitsManager.addEnemies(enemies.invaders)

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_LEFT:
            spaceship.moveLeft()
        elif key == curses.KEY_RIGHT:
            spaceship.moveRight()
        elif key == ord(' '):
            spaceship.shoot()

        # Check if there is no enemies
        if(Board.score == 55):
            Movements.invaders.clear()
            stdscr.addstr(15, 40, "You Win!!!")
            return

        board.__init__(stdscr)
        defense.__init__(stdscr)
        spaceship.print()
        enemies.print()
        hitsManager.checkHits()
        stdscr.refresh()
        sleep(0.03)

if __name__ == '__main__':
    curses.wrapper(main)
