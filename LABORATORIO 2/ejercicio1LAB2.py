import math

class MiPunto:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def distancia(self, *args):
        if len(args) == 1 and isinstance(args[0], MiPunto):
            dx = self._x - args[0]._x
            dy = self._y - args[0]._y
            return math.sqrt(dx**2 + dy**2)
        elif len(args) == 2:
            dx = self._x - args[0]
            dy = self._y - args[1]
            return math.sqrt(dx**2 + dy**2)

p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print(p1.distancia(p2))
