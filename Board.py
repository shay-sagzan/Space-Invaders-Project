import curses

class Board:
    # Initial Variables
    score = 0
    
    def __init__(self, stdscr: curses.window):
        """The function initiate the board with the score"""
        # Update Score
        sh, sw = stdscr.getmaxyx()
        score_text = "Score: {}".format(self.score)
        stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
