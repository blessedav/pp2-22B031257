import pygame, pygame.math, sys, random, time
import psycopg2 as pgsql
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size) # create a rectangle
            pygame.draw.rect(screen, (0, 102, 0), block_rect) # draw the rectangle
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size) # create a rectangle
        if glapplemode == 0:
            pygame.draw.rect(screen, (255, 255, 0), fruit_rect) # draw the rectangle
        else:
            pygame.draw.rect(screen, (255, 0, 0), fruit_rect)
    
    def randomize(self):
        global glapplemode
        glapplemode = random.randint(0, 5)
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y) # create an x and y position

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.fail = False
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        if not self.fail:
           screen.blit(bg, (0, 0))
           self.fruit.draw_fruit()
           self.snake.draw_snake()
           self.draw_score()
        else:
            screen.blit(bgdead, (0, 0))
            text = "SCORE: " + str(cntapple + cntglapple * 5)
            surface = game_font.render(text, True, (255, 255, 255))
            score_rect = surface.get_rect(center = (10 * cell_size, 15 * cell_size))
            text2 = "LEVEL: " + str(1 + (cntapple + cntglapple) // 10)
            surface2 = game_font.render(text2, True, (255, 255, 255))
            score_rect2 = surface2.get_rect(center = (10 * cell_size, 16 * cell_size))
            screen.blit(surface, score_rect)
            screen.blit(surface2, score_rect2)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            if glapplemode == 0:
                global cntglapple
                cntglapple += 1
            else:
                global cntapple
                cntapple += 1
            self.fruit.randomize() # reposition the fruit 
            self.snake.add_block() # add another block to the snake

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()    # check if snake is outside of the screen 
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over() # check if snake hits itself

    def game_over(self):
        self.fail = True   
    
    def draw_score(self):
        level_text = "Your level is: " + str(1 +(cntapple + cntglapple) // 10)
        level_surface = game_font.render(level_text, True, (0, 0, 0))
        level_rect = level_surface.get_rect(center = (10 * cell_size, 20))

        score_text = str(cntapple + cntglapple * 5)
        score_surface = game_font.render(score_text, True, (0, 0, 0))
        score_x = int(cell_size * 20 - 60)
        score_y = int(cell_size * 20 - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)
        screen.blit(level_surface, level_rect)

    

pygame.init()
cell_size = 40
cell_number = 20
speed = 200
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("$nake")
clock = pygame.time.Clock()
bg = pygame.image.load("bg.png").convert_alpha()
bgdead = pygame.image.load("bgdead.png").convert_alpha()
game_font = pygame.font.Font(None, 25)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, speed)


glapplemode = 1
timer = 0
cntapple = 0
cntglapple = 0
main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE and main_game.fail == False:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if  event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)


    if glapplemode == 0:
        timer += 1
    if glapplemode == 0 and timer >= 500:
        glapplemode = random.randint(1, 5)
        timer = 0
        
    speed = 200 - ((len(main_game.snake.body) - 3) // 10) * 5
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
