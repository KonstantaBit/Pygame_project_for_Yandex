import math
import pygame as pg
import numpy as np
from numba import njit
from physical_objects import BaseObject
from structure_classes import Field


def render_skybox(screen_array, cam_az, app_width):
    offset = 0
    left = screen_array[:offset]
    right = screen_array[offset:]
    result_array = np.stack((*right, *left))
    return result_array


@njit(fastmath=True)
def ray_cast(screen_array,
             map_width, map_height,
             color_map, height_map,
             app_height, scale_height,
             width, height, screen_x, screen_y,
             cam_x, cam_y, cam_z,
             cam_ax, cam_ay, cam_az,
             ray_distance, ray_count,
             jumping, fov
             ):
    result_array = screen_array
    step = 1
    ray_angle = math.radians(cam_az) - fov / 2
    for num_ray in range(ray_count):
        depth = 1
        first_contact = False
        height_buffer = 0
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
                        for arr_y in range(height_on_screen, height_buffer):
                            if arr_y + screen_y >= app_height:
                                break
                            result_array[num_ray][arr_y + screen_y] = color_map[x][y]
                        height_buffer = height_on_screen
        ray_angle += fov / ray_count
    return result_array


class Camera:
    def __init__(self, app, target: BaseObject, field: Field):
        # Внешние связи
        self.app = app
        self.target = target
        self.field = field

        # Настройки камеры
        self.FOV = math.radians(120)  # В градусах
        self.view_distance = 5000  # В пикселях
        self.scale_height = 800  # В пикселях
        self.rays_count = field.width
        self.jumping = 0  # Область значений: 0 - 0.0001

    def update(self):
        self.target.update()
        self.screen_array = np.zeros((self.app.WIDTH, self.app.HEIGHT, 3), dtype=int)
        self.screen_array = render_skybox(self.app.skybox.copy(), self.target.ang.z, self.app.WIDTH)
        self.screen_array = ray_cast(self.screen_array,
                                     self.app.map_width, self.app.map_height,
                                     self.app.color_map, self.app.height_map,
                                     self.app.HEIGHT, self.scale_height,
                                     self.field.width, self.field.height,
                                     self.field.screen_x, self.field.screen_y,
                                     self.target.pos.x, self.target.pos.y, self.target.pos.z,
                                     self.target.ang.x, self.target.ang.y, self.target.ang.z,
                                     self.view_distance, self.rays_count, self.jumping, self.FOV)
        pg.surfarray.blit_array(self.app.screen, self.screen_array)



