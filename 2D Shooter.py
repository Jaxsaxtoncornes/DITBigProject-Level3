import sys
import pygame

pygame.init()

SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter")

clock = pygame.time.Clock()

BACKGROUND_COLOUR = (255, 255, 255)
black = (0,0,0)


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

    def movement(self, keys):
        if keys[self.left]:
            self.x -= self.speed
        
        if keys[self.right]:
            self.x += self.speed
        
        if keys[self.up]:
            self.y -= self.speed
        
        if keys[self.down]:
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def boundrys(self):
        if self.x < 0:
            self.x = 0

        if self.y < 0:
            self.y = 0

        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

        if self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height

        self.rect.x = self.x        
        self.rect.y = self.y


    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.colour,
            (self.x, self.y, self.width, self.height)
        )

    def collision(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False

player1 = Players(
    0, 800,
    (225, 0, 0),
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s    
)

player2 = Players(
    1400, 800,
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

    player1.movement(keys)

    if player1.collision(player2):
        player1.x -= player1.speed
        player1.rect.x = player1.x

    player1.boundrys()

    player2.movement(keys)

    if player2.collision(player1):
        player2.x -= player2.speed
        player2.rect.x = player2.x

    player2.boundrys()  

    screen.fill(BACKGROUND_COLOUR)

    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()