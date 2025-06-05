import curses
from game import Game

def main_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(5, 10, "=== Snake Game ===")
    stdscr.addstr(7, 10, "1 - Start Game")
    stdscr.addstr(8, 10, "2 - Exit")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            game = Game(stdscr)
            game.run()
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(12, 10, "Press any key to return to menu...")
            stdscr.getch()
            return main_menu(stdscr)  # volver al menú
        elif key == ord('2'):
            break

if __name__ == "__main__":
    curses.wrapper(main_menu)