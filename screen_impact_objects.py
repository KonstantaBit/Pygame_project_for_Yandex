import math
import pygame as pg

from physical_objects import *
from voxel_render import VoxelRender


class ScreenImpact:
    def __init__(self, app):
        self.app = app

    def impact(self):
        pass


class SkyBox(ScreenImpact):
    pass


class GUI(ScreenImpact):
    pass


class Particles(ScreenImpact):
    pass


class Polygons(ScreenImpact):
    pass


class Camera(Control, ScreenImpact):
    def __init__(self, pos, ang, app, width=0, height=0, screen_x=0, screen_y=0):
        BaseObject.__init__(self, pos, ang)
        ScreenImpact.__init__(self, app)
        self.width = width
        self.height = height
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.FOV = math.radians(110)  # В градусах было
        self.view_distance = 50000

    def impact(self):
        n = VoxelRender(self, self.app)
        n.update()
        n.draw()


class DebugMap(ScreenImpact):
    def __init__(self, app, obj: BaseObject):
        ScreenImpact.__init__(self, app)
        self.obj = obj

    def impact(self):
        print(self.obj.pos, self.obj.ang, sep=' - ')
        pg.draw.circle(self.app.screen, 'white', (self.obj.pos.x, self.obj.pos.y), 10)
        pg.draw.line(self.app.screen, 'red', (self.obj.pos.x, self.obj.pos.y),
                     (self.obj.pos.x + 100 * math.cos(math.radians(self.obj.ang.az)),
                      self.obj.pos.y + 100 * math.sin(math.radians(self.obj.ang.az))),
                     5)
