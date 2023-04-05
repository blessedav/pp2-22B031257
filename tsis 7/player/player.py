import os
import pygame as pg

pg.init()

class SOUND:
    def __init__(self, path_to_sound, path_to_covers):
        self.sound = pg.mixer.Sound('Muz\\' + path_to_sound)
        self.photo = pg.image.load('AssetsPlayer\\covers\\' + path_to_covers)
        self.is_playing = True

    def placePhoto(self, screen):
        self.photo = pg.transform.scale(self.photo, (200, 200))
        screen.blit(self.photo, (111, 93))

path_to_sound = os.listdir('Muz\\')
path_to_covers = os.listdir('AssetsPlayer\\covers\\')
path_to_sound.sort()
path_to_covers.sort()

sounds = []

for index in zip(path_to_covers, path_to_sound):
    print(index)
    print(index[0])
    sound = SOUND(path_to_covers = index[0], path_to_sound = index[1])
    sounds.append(sound)

screen = pg.display.set_mode((400, 500))

BACKGROUND = pg.image.load('AssetsPlayer/Back.png').convert()
screen.blit(BACKGROUND, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto(screen)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())
            if 200 <= pg.mouse.get_pos()[0] <= 235 and 343 <= pg.mouse.get_pos()[1] <= 366:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 147 <= pg.mouse.get_pos()[0] <= 182 and 343 <= pg.mouse.get_pos()[1] <= 366:
                pg.mixer.stop()
                sounds[sound_index].is_playing = True
                if(sound_index == 0):
                    sound_index = len(sounds)
                sound_index -= 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
            elif 243 <= pg.mouse.get_pos()[0] <= 278 and 343 <= pg.mouse.get_pos()[1] <= 366:
                pg.mixer.stop()
                sounds[sound_index].is_playing = True
                if(sound_index == len(sounds) - 1):
                    sound_index = -1
                sound_index += 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
    pg.display.flip()