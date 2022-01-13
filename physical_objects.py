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
    def __init__(self, pos, ang):
        super().__init__(pos, ang)
        self.vel = 5
        self.angle_vel = 1

    def update(self):
        print(self.ang.z)
        if self.ang.z > 360:
            self.ang.z = 0
        if self.ang.z < 0:
            self.ang.z = 359
        sin_a = math.sin(math.radians(self.ang.z))
        cos_a = math.cos(math.radians(self.ang.z))

        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_UP]:
            self.ang.y += self.vel
        if pressed_key[pg.K_DOWN]:
            self.ang.y -= self.vel

        if pressed_key[pg.K_LEFT]:
            self.ang.z -= self.angle_vel
        if pressed_key[pg.K_RIGHT]:
            self.ang.z += self.angle_vel

        if pressed_key[pg.K_q]:
            self.pos.z += self.vel
        if pressed_key[pg.K_e]:
            self.pos.z -= self.vel

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