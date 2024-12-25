import pygame
import random

sw, sh = 500, 400
ms = 5
fs = 72

pygame.init()

bg_img = pygame.transform.scale(pygame.image.load("bg.jpg"), (sw, sh))

font = pygame.font.SysFont("Times New Roman", fs)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, sw - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, sh - self.rect.height), 0)

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Sprite Collides")
allsprite = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color("yellow"), 10, 20)
sprite1.rect.x, sprite1.rect.y = random.randint(0, sw - sprite1.rect.width), random.randint(0, sh - sprite1.rect.height)
allsprite.add(sprite1)

sprite2 = Sprite(pygame.Color("green"), 10, 20)
sprite2.rect.x, sprite2.rect.y = random.randint(0, sw - sprite2.rect.width), random.randint(0, sh - sprite2.rect.height)
allsprite.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    screen.blit(bg_img, (0, 0))

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * ms
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * ms
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            allsprite.remove(sprite2)
            won = True

    allsprite.update()
    allsprite.draw(screen)

    if won:
        win_text = font.render("Victory!", True, pygame.Color('black'))
        text_rect = win_text.get_rect(center=(sw // 2, sh // 2))
        screen.blit(win_text, text_rect)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
