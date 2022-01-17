import sys
import os
import pygame as pg


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


class GUI:
    def __init__(self, app):
        self.app = app
        self.running = False
        self.frame = 1
        self.last = 0
        self.snd = pg.mixer.Sound('data/snd.mp3')

    def update(self):
        if self.app.clicked_left:
            self.running = True
        if self.running:
            self.last += self.app.clock.get_time()
            self.app.screen.blit(load_image(f'gun_{self.frame}.png'), (400, 220))

            if self.last > 70:
                self.last = 0
                self.frame += 1
                if self.frame == 3:
                    self.snd.play()
        else:
            self.app.screen.blit(load_image(f'gun_1.png'), (400, 220))
        if self.frame == 5:
            self.frame = 1
            self.running = False
