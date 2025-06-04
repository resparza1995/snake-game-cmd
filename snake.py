from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

class Snake:
    def __init__(self, y, x):
        self.body = [(y, x+1), (y, x), (y, x-1)]
        self.grow_next = False

    def next_head_position(self, key):
        y, x = self.body[0]
        if key == KEY_UP:
            y -= 1
        elif key == KEY_DOWN:
            y += 1
        elif key == KEY_LEFT:
            x -= 1
        elif key == KEY_RIGHT:
            x += 1  
        return (y, x)
    
    def move(self, new_head):
        self.body.insert(0, new_head)
        if not self.grow_next:
            self.body.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True