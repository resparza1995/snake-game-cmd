import curses 
import random
from snake import Snake
from food import Food

class Game:
    speed = 100  # milliseconds
    opposite_directions = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT
    }

    def show_score(self):
        self.win.addstr(self.sh // 2, self.sw // 2 - 5, f"Score: {self.score}")
        self.win.refresh()
        curses.napms(1000)

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.sh, self.sw = curses.LINES, curses.COLS
        self.win = curses.newwin(self.sh, self.sw, 0, 0)
        self.win.keypad(True)
        self.win.nodelay(True)
        self.win.border(0)

        self.snake = Snake(self.sh // 2, self.sw // 2)
        self.food = Food(self.sh, self.sw, self.snake.body)
        self.win.addch(self.food.position[0], self.food.position[1], '*')
        self.key = curses.KEY_RIGHT
        self.score = 0

    def is_collision(self, new_head):
        if (new_head[0] in [0, self.sh - 1] or
            new_head[1] in [0, self.sw - 1] or
            new_head in self.snake.body):
            return True
        return False

    def increase_speed(self):
        if self.score % 1 == 0 and self.speed > 30:
            self.speed -= 10

    def eat_food(self, new_head):
        if new_head == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.spawn(self.sh, self.sw, self.snake.body)
            self.win.addch(self.food.position[0], self.food.position[1], '*')
            self.increase_speed()
        else:
            tail = self.snake.body[-1]
            self.win.addch(tail[0], tail[1], ' ')
    
    def print_snake(self):
        for segment in self.snake.body[1:]:
            self.win.addch(segment[0], segment[1], '#')
        self.win.addch(self.snake.body[0][0], self.snake.body[0][1], '@')

    def run(self):
        while True:
            self.win.timeout(self.speed)
            next_key = self.win.getch()
            if next_key != -1 and next_key != self.opposite_directions.get(self.key, -1):
                self.key = next_key
            
            new_head = self.snake.next_head_position(self.key)
            if self.is_collision(new_head):
                break

            self.eat_food(new_head)
            self.snake.move(new_head)
            self.print_snake()

            # show score
            self.win.addstr(0, 2, f'Score: {self.score} ')

        self.show_score()
        return self.score



