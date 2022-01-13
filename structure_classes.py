class Cords:
    def __init__(self, x: float, y: float, z: float):
        buff = [type(i) for i in [x, y, z] if not (isinstance(i, float) or isinstance(i, int))]
        if len(buff):
            raise TypeError(f"Expected type 'float', got {type(buff[0])} instead")
        del buff
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Angles:
    def __init__(self, x: float, y: float, z: float):
        buff = [type(i) for i in [x, y, z] if not (isinstance(i, float) or isinstance(i, int))]
        if len(buff):
            raise TypeError(f"Expected type 'float', got {type(buff[0])} instead")
        del buff
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Field:
    def __init__(self, screen_x, screen_y, width, height):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.width = width
        self.height = height
