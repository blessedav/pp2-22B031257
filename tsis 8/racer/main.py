import pygame
import sys
from pygame.locals import *
import random
import time
pygame.init()

FramePerSec = pygame.time.Clock()
FPS = 60
SPEED = 5
SCORE = 0
STARS = 0
# Colors
BLUE = pygame.Color(0,0,255) 
BLACK = pygame.Color(0,0,0) 
WHITE = pygame.Color(255,255,255) 
GREY = pygame.Color(128,128,128) 
RED = pygame.Color(255,0,0) 
# setup FONTS
font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")
# Create window display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
# ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.bottom > 600:
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
#PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        global STARS
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
        # Collision with a star
        collided_stars = pygame.sprite.spritecollide(self,Stars,True)
        for star in collided_stars:
            STARS+=1
            if len(Stars)<3:
                for i in range(random.randint(1,2)):
                    new_star = STAR()
                    Stars.add(new_star)
                    all_sprites.add(new_star)
#STAR         
class STAR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("star.png")
        # Scale PNG and update rect.width and rect.height 
        self.image = pygame.transform.scale(self.image,(self.image.get_width() // 3, self.image.get_height() // 3))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
        self.rect.width //= 3
        self.rect.height //= 3
    # Same move as Enemy
    def move(self):
        self.rect.move_ip(0,SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
        

P1 = Player()
E1 = Enemy()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
Stars = pygame.sprite.Group()
for i in range(random.randint(1,3)):
    star = STAR()
    Stars.add(star)
all_sprites = pygame.sprite.Group()
all_sprites.add(Stars)
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new USER event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED+=0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    stars = font_small.render(str(STARS),True,BLACK)
    if STARS < 10:
        DISPLAYSURF.blit(stars, (350,10))
    else: 
        DISPLAYSURF.blit(stars, (320,10))
    # moves and redraws all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(FPS)