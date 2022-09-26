import curses

class Utilities:
    # Initial Variables
    shape: str
    shots = []
    bullet: str
    shotDir: int
    isAlien: bool
    color: str

    def __init__(self, stdscr: curses.window):
        """The function initiate the variables of different entities"""
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.shots = []
        self.isDead = False
        self.pos = [0, 0]


    @classmethod
    def setHitsManager(cls, hitsManager):
        Utilities.hitsManager = hitsManager

    def print(self):
        if self.isDead:
            self.gameOver()
            return
        self.stdscr.addstr(*self.pos, self.shape)  
        for i, shot in enumerate(self.shots):
            self.stdscr.addstr(*shot, self.bullet, self.color)
            shot[0] += self.shotDir
            if not 0 <= shot[0] <= self.height-1:
                del self.shots[i]
            self.hitsManager.addEnemyBullet(
                shot, self) if self.isAlien else self.hitsManager.addPlayerBullet(shot, self)

    def shoot(self):
        shotPos = self.pos[:]
        shotPos[0] += self.shotDir
        self.shots.append(shotPos)

    def kill(self):
        self.isDead = True

    def destroyShot(self, shot):
        if shot in self.shots:
            self.shots.remove(shot)

    def gameOver(self):
            self.stdscr.addstr(5, 20, "Game Over!!!")
