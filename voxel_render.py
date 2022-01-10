import pygame as pg
import numpy as np
import math
from numba import njit


height_map_img = pg.image.load('data/H1.png')
height_map = pg.surfarray.array3d(height_map_img)

color_map_img = pg.image.load('data/C1.png')
color_map = pg.surfarray.array3d(color_map_img)

map_height = len(height_map[0])
map_width = len(height_map)


@njit(fastmath=True)
def ray_cast(screen_height, cam_x, cam_y, cam_z, cam_ax,
             cam_ay, cam_az, ray_distance, ray_angle, jumping, scale_height):
    y_buffer = np.zeros((screen_height, 3))
    depth = 0
    step = 1
    height_buffer = screen_height
    while depth < ray_distance:
        depth += step
        step += jumping
        x = int(cam_x + depth * math.cos(ray_angle))
        if 0 < x < map_width:
            y = int(cam_y + depth * math.sin(ray_angle))
            if 0 < y < map_height:
                height_on_screen = int((cam_z - height_map[x][y][0]) /
                                       (depth * math.cos(math.radians(cam_az) - ray_angle)) * scale_height + cam_ay)
                if 0 <= height_on_screen <= height_buffer:
                    for screen_y in range(height_on_screen, height_buffer):
                        y_buffer[screen_y] = color_map[x][y]
                    height_buffer = height_on_screen
    return y_buffer


class VoxelRender:
    def __init__(self, cam, app):
        self.app = app
        self.cam = cam
        self.screen_array = np.zeros((cam.width, cam.height, 3), dtype=int)
        self.scale_height = 800
        self.rays_count = cam.width  # Мы же желаем лучшего графона -_-
        self.ray_width = cam.width / self.rays_count
        self.scaling = 1
        """
        для увеличения проиводительности, шаг луча каждый раз будет всё больше и больше,
        если равен = 0, то эффекта не будет
        """
        self.jumping = 0

    def update(self):
        ray_angle = math.radians(self.cam.ang.az) - self.cam.FOV / 2
        delta_angle = self.cam.FOV / self.rays_count
        for ray_num in range(self.rays_count):
            self.screen_array[ray_num] = ray_cast(self.cam.height, self.cam.pos.x, self.cam.pos.y, self.cam.pos.z,
                                                  self.cam.ang.ax, self.cam.ang.ay, self.cam.ang.az,
                                                  self.cam.view_distance, ray_angle, self.jumping, self.scale_height)
            ray_angle += delta_angle

    def draw(self):
       pg.surfarray.blit_array(self.app.screen, self.screen_array)
