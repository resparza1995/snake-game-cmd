import curses
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = curses.LINES, curses.COLS
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.nodelay(True)
    win.border(0)

    snake = [(sh//2, sw//2 + 1), (sh//2, sw//2), (sh//2, sw//2 - 1)]
    food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
    win.addch(food[0], food[1], '*')

    key = curses.KEY_RIGHT
    score = 0

    while True:
        win.timeout(100)
        next_key = win.getch()

        # Diccionario de direcciones opuestas
        opposite = {
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_RIGHT: curses.KEY_LEFT
        }

        # Solo actualiza si la nueva dirección no es la opuesta
        if next_key != -1 and next_key != opposite.get(key, -1):
            key = next_key

        y, x = snake[0]
        if key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1

        new_head = (y, x)

        if (y in [0, sh - 1] or x in [0, sw - 1] or new_head in snake):
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            while True:
                food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
                if food not in snake:
                    break
            win.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        # Dibujar cuerpo
        for segment in snake[1:]:
            win.addch(segment[0], segment[1], '#')
        # Dibujar cabeza
        win.addch(snake[0][0], snake[0][1], '@')

    curses.endwin()
    print(f"Game Over. Score: {score}")

curses.wrapper(main)
