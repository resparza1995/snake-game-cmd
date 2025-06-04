import random 

class Food:
    def __init__(self, sh, sw, snake_body):
        self.position = ()
        self.spawn(sh, sw, snake_body)

    def spawn(self, sh, sw, snake_body):
        while True:
            pos = (random.randint(1, sh-2), random.randint(1, sw-2))
            if pos not in snake_body:
                self.position = pos
                break