# Важные либы
import time

import pygame as pg
import sys
import random
from PIL import Image
from GUI import GUI

# для объектов
from Camera import Camera
from physical_objects import Player, Bottle
from structure_classes import Field


class App:
    def __init__(self, map):
        self.map = map
        self.count = 0
        self.init_settings()
        self.init_map()
        self.init_bridges()


    def init_settings(self):
        pg.mouse.set_visible(False)
        with open('config.txt', 'r') as f:
            config = {i.split('=')[0]: i.split('=')[1] for i in f.read().split('\n')}
        pg.init()
        self.running = True
        self.SIZE = self.WIDTH, self.HEIGHT = (int(config['WIDTH']), int(config['HEIGHT']))
        self.screen = pg.display.set_mode(self.SIZE, pg.SCALED)
        self.clock = pg.time.Clock()
        self.FPS = int(config['FPS'])
        self.DISPLAY_FPS = bool(int(config['DISPLAY_FPS']))

    def init_map(self):
        self.color_map_img = pg.surfarray.array3d(pg.image.load(f'data/C{self.map}W.png'))
        self.height_map_img = pg.surfarray.array3d(pg.image.load(f'data/D{self.map}.png'))
        self.color_map = self.color_map_img
        self.height_map = self.height_map_img
        self.map_height = len(self.height_map[0])
        self.map_width = len(self.height_map)
        buff = Image.open('data/default_skybox.png')
        out = buff.resize(self.SIZE)
        out.save('data/work_skybox.png')
        self.skybox = pg.surfarray.array3d(pg.image.load('data/work_skybox.png'))
        self.cam = Camera(self, Player(self, (540, 170, 200), (0, 300, 180)), Field(0, 0, *self.SIZE))
        self.gui = GUI(self)
        self.objects = [Bottle(self, 770, 260, 5, (255, 200, 80))]
        for i in range(100):
            self.objects.append(Bottle(self, random.randint(10, self.map_width - 10),
                                       random.randint(10, self.map_height - 10),
                                       5, (random.randint(10, 200), 100, random.randint(10, 200))))

    def init_bridges(self):
        self.clicked_left = False
        self.clicked_right = False

    def load_map(self):
        self.color_map = pg.surfarray.array3d(pg.image.load(f'data/C{self.map}W.png'))
        self.height_map = pg.surfarray.array3d(pg.image.load(f'data/D{self.map}.png'))

    def update(self):
        for i in self.objects:
            i.update()
        self.cam.update()
        self.gui.update()

    def draw(self):
        pg.display.flip()
        self.screen.fill(0)

    def run(self):
        while self.running:
            self.update()
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicked_left = True
                    if event.button == 3:
                        print(5)
                        self.clicked_right = True
                else:
                    self.clicked_right = False
                    self.clicked_left = False
            self.clock.tick(self.FPS)
            name = 'Lonely Shooter'
            if self.DISPLAY_FPS:
                name += f' - FPS: {round(self.clock.get_fps(), 1)}'
            pg.display.set_caption(name)

    def end(self):
        f1 = pg.font.Font(None, 36)
        text1 = f1.render(f'Ваш счет: {self.count}', True,
                          (180, 0, 0))
        self.screen.blit(text1, (10, 50))
        self.draw()
        time.sleep(3)
        self.running = False

    def terminate(self):
        self.end()
        pg.quit()
        sys.exit()
