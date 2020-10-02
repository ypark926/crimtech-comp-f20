import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    appleEaten = False

    def __init__(self):
        pass

    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir

    def collision(self, x, y):
        if y > HEIGHT or y < 0 or x > WIDTH or x < 0:
            return True

        for i in range(1, len(self.body)):
            if (self.body[0][0] == self.body[i][0]) and (self.body[0][1] == self.body[i][1]):
                return True

        return False

    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self, apple):
        self.appleEaten = False
        x, y = DIR[self.direction]
        temp = (0,0)
        for i in range(len(self.body)):
            coord1, coord2 = self.body[i]
            (move1, move2) = temp
            if i == 0:
                self.body[i] = (coord1 + x, coord2 + y)
            else:
                self.body[i] = (move1, move2)
            temp = (coord1, coord2)

        if self.collision(self.get_head()[0], self.get_head()[1]):
            self.kill()

        if self.get_head() == apple.position:
            self.appleEaten = True
            apple.place(self)
            self.l += 1
            self.body.append(temp)


    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)

    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self, snake):
        self.place(snake)

    def place(self, snake):
        applepos = (random.randint(0,23), random.randint(0,23))
        for i in range(len(snake.body)):
            if i == applepos:
                applepos = (random.randint(0,23), random.randint(0,23))
        self.position = applepos

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    font = pygame.font.Font(pygame.font.get_default_font(), 16)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple(snake)

    score = 0

    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(10)
        snake.check_events()
        draw_grid(surface)
        snake.move(apple)

        snake.draw(surface)
        apple.draw(surface)
        # TODO: see section 5, "Eating the Apple".
        if snake.appleEaten:
            score += 1
            print('The snake ate an apple!')
        scoreDisplay = font.render(str(score), False, (0, 0, 0))
        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()
