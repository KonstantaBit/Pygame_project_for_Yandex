import pygame as pg
import math
from structure_classes import Cords, Angles


class BaseObject:
    def __init__(self, pos: tuple, ang: tuple):
        if not len(pos) == len(ang) == 3:
            raise ValueError
        self.pos = Cords(*pos)
        self.ang = Angles(*ang)

    def update(self):
        pass


class Player(BaseObject):
    def __init__(self, app, pos, ang):
        super().__init__(pos, ang)
        self.app = app
        self.vel = 1
        self.angle_vel = 1

    def update(self):
        self.gravity()
        self.key_control()
        self.mouse_control()

    def gravity(self):
        if self.app.height_map[int(self.pos.x)][int(self.pos.y)][0] + 5 <= self.pos.z:
            self.pos.z -= 3
        if not self.app.height_map[int(self.pos.x)][int(self.pos.y)][0] + 5 <= self.pos.z:
            self.pos.z += 3

    def key_control(self):
        sin_a = math.sin(math.radians(self.ang.z))
        cos_a = math.cos(math.radians(self.ang.z))

        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_UP]:
            self.ang.y += self.vel
        if pressed_key[pg.K_DOWN]:
            self.ang.y -= self.vel

        if pressed_key[pg.K_ESCAPE]:
            self.app.end()
        if pressed_key[pg.K_w]:
            self.pos.x += self.vel * cos_a
            self.pos.y += self.vel * sin_a
        if pressed_key[pg.K_s]:
            self.pos.x -= self.vel * cos_a
            self.pos.y -= self.vel * sin_a
        if pressed_key[pg.K_a]:
            self.pos.x += self.vel * sin_a
            self.pos.y -= self.vel * cos_a
        if pressed_key[pg.K_d]:
            self.pos.x -= self.vel * sin_a
            self.pos.y += self.vel * cos_a

    def mouse_control(self):
        sens = 0.7
        if pg.mouse.get_focused():
            offset = pg.mouse.get_pos()[0] - self.app.WIDTH // 2
            self.ang.z += offset * sens
            offset = pg.mouse.get_pos()[1] - self.app.HEIGHT // 2
            pg.mouse.set_pos(self.app.WIDTH // 2, self.app.HEIGHT // 2)
            self.ang.y += offset * -sens * 2.5


class Bottle:
    def __init__(self, app, x, y, size, color):
        self.x = int(x)
        self.app = app
        self.y = int(y)
        self.size = size
        self.color = color
        self.update()

    def brush(self):
        for i in range(self.size):
            for j in range(self.size):
                self.app.height_map[self.x + i][self.y + j][0] -= 5

    def update(self):
        for i in range(self.size):
            for j in range(self.size):
                self.app.height_map[self.x + i][self.y + j][0] = 40
        for i in range(self.size):
            for j in range(self.size):
                self.app.color_map[self.x + i][self.y + j] = self.color
