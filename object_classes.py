from structure_classes import Cords, Angles


class Object:
    def __init__(self, pos: Cords, ang: Angles):
        if not isinstance(pos, Cords):
            raise TypeError(f"Expected type 'Cords', got {type(pos)} instead")
        if not isinstance(ang, Angles):
            raise TypeError(f"Expected type 'Angles', got {type(ang)} instead")
        self.pos = pos
        self.ang = ang


class Camera(Object):
    def __init__(self, pos, ang):
        super().__init__(pos, ang)
        pass

