from threading import Thread


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


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return
