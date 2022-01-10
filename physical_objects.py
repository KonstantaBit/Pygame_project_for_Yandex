from structure_classes import Cords, Angles
import math
import pygame as pg


class BaseObject:
    def __init__(self, pos: Cords, ang: Angles):
        if not isinstance(pos, Cords):
            raise TypeError(f"Expected type 'Cords', got {type(pos)} instead")
        if not isinstance(ang, Angles):
            raise TypeError(f"Expected type 'Angles', got {type(ang)} instead")
        self.pos = pos
        self.ang = ang


class PhysicObject(BaseObject):
    pass


class Control(BaseObject):
    def update(self):
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_UP]:
            self.ang.ay += self.vel
        if pressed_key[pg.K_DOWN]:
            self.pitch -= self.vel