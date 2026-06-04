import sys
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter")

clock = pygame.time.Clock()

BACKGROUND_COLOUR = (255, 255, 255)

player_colour = (225, 0, 0)
player_width = 25
player_height = 25

player_x = 300
player_y = 300
player_speed = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOUR)
 
    pygame.draw.rect(screen, player_colour, (player_x, player_y, player_width, player_height))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()