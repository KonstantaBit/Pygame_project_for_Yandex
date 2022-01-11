import pygame as pg
import numpy as np
import math
from numba import njit
from structure_classes import make_surface_rgba


height_map_img = pg.image.load('data/H1.png')
height_map = pg.surfarray.array3d(height_map_img)

color_map_img = pg.image.load('data/C1.png')
color_map = pg.surfarray.array3d(color_map_img)

map_height = len(height_map[0])
map_width = len(height_map)


@njit(fastmath=True)
def ray_cast(app_height, height, start_y_pos, cam_x, cam_y, cam_z, cam_ax,
             cam_ay, cam_az, ray_distance, ray_angle, jumping, scale_height):
    y_buffer = np.zeros((app_height, 4))
    depth = 0
    step = 1
    height_buffer = 0
    first_contact = False
    while depth < ray_distance:
        depth += step
        step += jumping
        x = int(cam_x + depth * math.cos(ray_angle))
        if 0 < x < map_width:
            y = int(cam_y + depth * math.sin(ray_angle))
            if 0 < y < map_height:
                height_on_screen = int((cam_z - height_map[x][y][0]) /
                                       (depth * math.cos(math.radians(cam_az) - ray_angle)) * scale_height + cam_ay)
                if not first_contact:
                    height_buffer = min(height_on_screen, height)
                    first_contact = True
                if height_on_screen < 0:
                    height_on_screen = 0
                if height_on_screen <= height_buffer:
                    for screen_y in range(height_on_screen, height_buffer):
                        if screen_y + start_y_pos >= app_height:
                            break
                        y_buffer[screen_y + start_y_pos] = [color_map[x][y][0], color_map[x][y][1],
                                                            color_map[x][y][2], 255]
                    height_buffer = height_on_screen
    return y_buffer


class VoxelRender:
    def __init__(self, cam, app):
        self.app = app
        self.cam = cam
        self.scale_height = 800
        self.rays_count = cam.width
        """
        для увеличения проиводительности, шаг луча каждый раз будет всё больше и больше,
        если равен = 0, то эффекта не будет
        UPD:
        Поверить не могу... это овермного дает производитьности
        """
        self.jumping = 0.05

    def update(self):
        self.screen_array = np.zeros((self.app.WIDTH, self.app.HEIGHT, 4), dtype=int)
        ray_angle = math.radians(self.cam.ang.az) - self.cam.FOV / 2
        delta_angle = self.cam.FOV / self.rays_count
        for ray_num in range(self.rays_count):
            if ray_num + self.cam.screen_x >= self.app.WIDTH:
                break
            self.screen_array[ray_num + self.cam.screen_x] = ray_cast(self.app.HEIGHT,
                                                                      self.cam.height, self.cam.screen_y,
                                                  self.cam.pos.x, self.cam.pos.y, self.cam.pos.z,
                                                  self.cam.ang.ax, self.cam.ang.ay, self.cam.ang.az,
                                                  self.cam.view_distance, ray_angle, self.jumping, self.scale_height)
            ray_angle += delta_angle

    def draw(self):
        surface = make_surface_rgba(self.screen_array)
        self.app.screen.blit(surface, (0, 0))
