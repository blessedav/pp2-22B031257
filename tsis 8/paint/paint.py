import pygame
import random

screen = pygame.display.set_mode((900, 700))

pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)

radius = 5


def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)


try :
    while True :
        e = pygame.event.wait()

        if e.type == pygame.QUIT :
            raise StopIteration

        if e.type == pygame.MOUSEBUTTONDOWN :
            color = (random.randrange(256), random.randrange(
                256), random.randrange(256))
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONUP :
            draw_on = False
        if e.type == pygame.MOUSEMOTION :
            if draw_on :
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos
        pygame.display.flip()

except StopIteration :
    pass

pygame.quit()