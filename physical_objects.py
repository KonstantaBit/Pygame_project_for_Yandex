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
        ay_speed = 3
        az_speed = 3
        velocity = 5
        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_UP]:
            self.ang.ay += ay_speed
        if pressed_key[pg.K_DOWN]:
            self.ang.ay -= ay_speed
        if pressed_key[pg.K_LEFT]:
            self.ang.az -= az_speed
        if pressed_key[pg.K_RIGHT]:
            self.ang.az += az_speed
        if pressed_key[pg.K_q]:
            self.pos.z += velocity
        if pressed_key[pg.K_e]:
            self.pos.z -= velocity
        if pressed_key[pg.K_w]:
            self.pos.x += velocity * math.cos(math.radians(self.ang.az))
            self.pos.y += velocity * math.sin(math.radians(self.ang.az))
        if pressed_key[pg.K_s]:
            self.pos.x -= velocity * math.cos(math.radians(self.ang.az))
            self.pos.y -= velocity * math.sin(math.radians(self.ang.az))
        if pressed_key[pg.K_a]:
            self.pos.x += velocity * math.sin(math.radians(self.ang.az))
            self.pos.y -= velocity * math.cos(math.radians(self.ang.az))
        if pressed_key[pg.K_d]:
            self.pos.x -= velocity * math.sin(math.radians(self.ang.az))
            self.pos.y += velocity * math.cos(math.radians(self.ang.az))
