import sys
import pygame

pygame.init()

SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 800

BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 10
BULLET_DAMAGE = 20
SHOOT_COOLDOWN = 300

bullets = []

scores = {
    "player1": 0,
    "player2": 0,
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter")

clock = pygame.time.Clock()

BACKGROUND_COLOUR = (224, 255, 255)
black = (0,0,0)
yellow = (225, 225, 0)

font = pygame.font.Font(None, 40)

class Players:
    def __init__(self, x, y, colour, left, right, up, down, shoot):
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
        self.shoot = shoot

        self.health = 100

        self.facing = "right"

        self.last_shot = 0

    def movement(self, keys, other):

        if keys[self.left]:
            self.rect.x -= self.speed
            self.facing - "left"
        
        if keys[self.right]:
            self.rect.x += self.speed
            self.facing - "right"

        
        if self.collision(other):
            if keys[self.left]:
                self.rect.left = other.rect.right

            if keys[self.right]:
                self.rect.right = other.rect.left

        if keys[self.up]:
            self.rect.y -= self.speed
            self.facing - "up"
        
        if keys[self.down]:
            self.rect.y += self.speed
            self.facing - "down"

        if self.collision(other):
            if keys[self.up]:
                self.rect.top = other.rect.bottom

            if keys[self.down]:
                self.rect.bottom = other.rect.top

    def shoot_bullet(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot < SHOOT_COOLDOWN:
            return

        self.last_shot = current_time

        if self.facing == "right":
            bullet = pygame.Rect(
                self.rect.right,
                self.rect.centery - BULLET_HEIGHT // 2,
                BULLET_WIDTH,
                BULLET_HEIGHT
            )
            direction = 1

        elif self.facing == "left":
            bullet = pygame.Rect(
                self.rect.left - BULLET_WIDTH,
                self.rect.centery - BULLET_HEIGHT // 2,
                BULLET_WIDTH,
                BULLET_HEIGHT
            )
            direction = -1

        elif self.facing == "up":
            bullet = pygame.Rect(
                self.rect.centerx - BULLET_HEIGHT // 2,
                self.rect.top - BULLET_WIDTH,
                BULLET_WIDTH,
                BULLET_HEIGHT
            )
            direction = "up"

        else:
            bullet = pygame.Rect(
                self.rect.centerx - BULLET_HEIGHT // 2,
                self.rect.bottom,
                BULLET_WIDTH,
                BULLET_HEIGHT
            )
            direction = "down"

        bullets.append({
            "rect": bullet,
            "direction": direction,
            "owner": self
        })

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

    def draw_gun(self, screen):

        gun_width = 12
        gun_height = 6

        if self.facing == "right":
            gun = pygame.Rect(
                self.rect.right,
                self.rect.centery - gun_height // 2,
                gun_width,
                gun_height
            )

        elif self.facing == "left":
            gun = pygame.Rect(
                self.rect.left - gun_width,
                self.rect.centery - gun_height // 2,
                gun_width,
                gun_height
            )

        elif self.facing == "up":
            gun = pygame.Rect(
                self.rect.centerx - gun_height //2,
                self.rect.top - gun_width,
                gun_width,
                gun_height
            )

        else:
            gun = pygame.Rect(
                self.rect.centerx - gun_height //2,
                self.rect.bottom,
                gun_width,
                gun_height
            )

        pygame.draw.rect(screen, black, gun)

    def collision(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False

    def draw_health(self, screen, x, y):

        pygame.draw.rect(
            screen,
            black,
            (x, y, 200, 20)
        )

        pygame.draw.rect(
            screen,
            self.colour,
            (x, y, self.health * 2, 20)
        )
    

player1 = Players(
    0, 775,
    (225, 0, 0),
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s,
    pygame.K_f  
)

player2 = Players(
    1400, 775,
    (0, 0, 225),
    pygame.K_j,
    pygame.K_l,
    pygame.K_i,
    pygame.K_k,
    pygame.K_h
)

walls = [
    pygame.Rect(350, 100, 20, 500),
    pygame.Rect(1080, 100, 20, 500),
    pygame.Rect(600, 340, 250, 20),
]

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[player1.shoot]:
        player1.shoot_bullet()

    if keys[player2.shoot]:
        player2.shoot_bullet()

    old_rect1 = player1.rect.copy()
    old_rect2 = player2.rect.copy()

    player1.movement(keys, player2)
    player1.boundrys()

    player2.movement(keys, player1)
    player2.boundrys()

    for bullet in bullets:

        if bullet["direction"] == 1:
            bullet["rect"].x += BULLET_SPEED

        elif bullet["direction"] == -1:
            bullet["rect"].x += BULLET_SPEED

        elif bullet["direction"] == "up":
            bullet["rect"].y += BULLET_SPEED

        elif bullet["direction"] == "down":
            bullet["rect"].y += BULLET_SPEED 

    for bullet in bullets[:]:

        for wall in walls:
            if bullet["rect"].colliderect(wall):
                bullets.remove(bullet)
                break

        else:

            if bullet["owner"] != player1:
                if bullet["rect"].colliderect(player1.rect):

                    player1.health -= BULLET_DAMAGE
                    bullets.remove(bullet)

                    if player1.health <= 0:
                        scores["player2"] += 1

                        player1.rect.topleft = (0, 775)
                        player1.health = 100

            elif bullet["owner"] != player2:
                if bullet["rect"].colliderect(player2.rect):

                    player2.health -= BULLET_DAMAGE
                    bullets.remove(bullet)

                    if player2.health <= 0:
                        scores["player2"] += 1

                        player2.rect.topleft = (0, 775)
                        player2.health = 100

    for wall in walls:
        if player1.rect.colliderect(wall):
            player1.rect = old_rect1.copy()

        if player2.rect.colliderect(wall):
            player2.rect = old_rect2.copy()

    screen.fill(BACKGROUND_COLOUR)

    for wall in walls:
        pygame.draw.rect(screen, black, wall)

    for bullet in bullets:
        pygame.drawn.rect(screen, yellow, bullet["rect"])

    player1.draw(screen)
    player1.draw_gun(screen)

    player2.draw(screen)
    player2.draw_gun(screen)

    player1.draw_health(screen, 20, 20)
    player2.draw_health(screen, SCREEN_WIDTH - 220, 20)

    score_text = font.render(
        f"P1: {scores['player1']}  P2: {scores['player2']}",
        True,
        black
    )

    screen.blit(
        score_text,
        (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20)
    )

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()