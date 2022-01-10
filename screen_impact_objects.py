import math

from physical_objects import *
from voxel_render import VoxelRender


class ScreenImpact:

    def __init__(self, app):
        self.app = app


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
        self.view_distance = 1000

    def impact(self):
        n = VoxelRender(self, self.app)
        n.update()
        n.draw()