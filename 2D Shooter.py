import sys
import pygame

pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter")

clock = pygame.time.Clock()

BACKGROUND_COLOUR = (255, 255, 255)
black = (0,0,0)


class Players:
    def __init__(self):
        self.x = x
        self.y = y

        self.width = 25
        self.height = 25

        self.colour = colour

        self.speed = 4

        self.colour = (255, 0, 0)

    def movement(self, keys):
        if keys[self.left]:
            self.x -= self.speed
        
        if keys[self.right]:
            self.x += self.speed
        
        if keys[self.up]:
            self.y -= self.speed
        
        if keys[self.down]:
            self.y += self.speed

    def boundrys(self):
        if self.x < 0:
            self.x = 0

        if self.y < 0:
            self.y = 0

        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.colour,
            (self.x, self.y, self.width, self.height)
        )

player1 = Players(
    0, 800
    (225, 0, 0),
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s    
)

player2 = Players(
    1400, 800
    (0, 0, 225),
    pygame.K_j,
    pygame.K_l,
    pygame.K_i,
    pygame.K_k
)

player = Players()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player1.movement(keys)
    player1.boundrys()

    player2.movement(keys)
    player2.boundrys()  

    screen.fill(BACKGROUND_COLOUR)

    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()