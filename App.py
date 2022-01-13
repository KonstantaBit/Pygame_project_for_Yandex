# Важные либы
import numpy as np
import pygame as pg
import sys
import os
from PIL import Image

# для объектов
from Camera import Camera
from physical_objects import Player
from structure_classes import Field


class App:
    def __init__(self):
        self.init_settings()
        self.init_map()

    def init_settings(self):
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
        self.color_map = pg.surfarray.array3d(pg.image.load('data/C1.png'))
        self.height_map = pg.surfarray.array3d(pg.image.load('data/H1.png'))
        self.map_height = len(self.height_map[0])
        self.map_width = len(self.height_map)
        buff = Image.open('data/default_skybox.png')
        out = buff.resize(self.SIZE)
        out.save('data/work_skybox.png')
        self.skybox = pg.surfarray.array3d(pg.image.load('data/work_skybox.png'))

        self.objects = [Camera(self, Player((0, 0, 200), (0, 0, 45)), Field(0, 0, *self.SIZE))]

    def update(self):
        for i in self.objects:
            i.update()

    def draw(self):
        pg.display.flip()
        self.screen.fill(0)

    def run(self):
        while self.running:
            self.update()
            self.draw()

            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.clock.tick(self.FPS)

            name = 'Lonely Shooter'
            if self.DISPLAY_FPS:
                name += f' - FPS: {round(self.clock.get_fps(), 1)}'
            pg.display.set_caption(name)

    def end(self):
        self.running = False

    def terminate(self):
        self.end()
        pg.quit()
        sys.exit()
