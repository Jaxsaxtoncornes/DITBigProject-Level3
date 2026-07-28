import sys
import pygame

pygame.init()

SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 800
BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter")

clock = pygame.time.Clock()

BACKGROUND_COLOUR = (255, 255, 255)
black = (0,0,0)
yellow = (225, 225, 0)

bullets = []

class Players:
    def __init__(self, x, y, colour, left, right, up, down):
        self.x = x
        self.y = y

        self.width = 25
        self.height = 25

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.colour = colour
        self.speed = 4

        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def movement(self, keys, other):

        if keys[self.left]:
            self.rect.x -= self.speed
        
        if keys[self.right]:
            self.rect.x += self.speed
        
        if self.collision(other):
            if keys[self.left]:
                self.rect.left = other.rect.right

            if keys[self.right]:
                self.rect.right = other.rect.left

        if keys[self.up]:
            self.rect.y -= self.speed
        
        if keys[self.down]:
            self.rect.y += self.speed

        if self.collision(other):
            if keys[self.up]:
                self.rect.top = other.rect.bottom

            if keys[self.down]:
                self.rect.bottom = other.rect.top


    def boundrys(self):
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.colour,
            self.rect
        )

    def collision(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False
    

player1 = Players(
    0, 775,
    (225, 0, 0),
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s    
)

player2 = Players(
    1400, 775,
    (0, 0, 225),
    pygame.K_j,
    pygame.K_l,
    pygame.K_i,
    pygame.K_k
)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player1.movement(keys, player2)

    player1.boundrys()

    player2.movement(keys, player1)

    player2.boundrys()  

    screen.fill(BACKGROUND_COLOUR)

    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit(.