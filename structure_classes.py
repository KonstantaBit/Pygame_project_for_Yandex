import pygame as pg
import numpy as np


class Cords:
    def __init__(self, x: float, y: float, z: float):
        buff = [type(i) for i in [x, y, z] if not (isinstance(i, float) or isinstance(i, int))]
        if len(buff):
            raise TypeError(f"Expected type 'float', got {type(buff[0])} instead")
        del buff
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"


class Angles:
    def __init__(self, ax: float, ay: float, az: float):
        buff = [type(i) for i in [ax, ay, az] if not (isinstance(i, float) or isinstance(i, int))]
        if len(buff):
            raise TypeError(f"Expected type 'float', got {type(buff[0])} instead")
        del buff
        self.ax = float(ax)
        self.ay = float(ay)
        self.az = float(az)

    def __str__(self):
        return f"ax: {self.ax}, ay: {self.ay}, az: {self.az}"


def make_surface_rgba(array):
    """Returns a surface made from a [w, h, 4] numpy array with per-pixel alpha
    """
    shape = array.shape
    if len(shape) != 3 and shape[2] != 4:
        raise ValueError("Array not RGBA")

    # Create a surface the same width and height as array and with
    # per-pixel alpha.
    surface = pg.Surface(shape[0:2], pg.SRCALPHA, 32)

    # Copy the rgb part of array to the new surface.
    pg.pixelcopy.array_to_surface(surface, array[:, :, 0:3])

    # Copy the alpha part of array to the surface using a pixels-alpha
    # view of the surface.
    surface_alpha = np.array(surface.get_view('A'), copy=False)
    surface_alpha[:, :] = array[:, :, 3]

    return surface
