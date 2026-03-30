import math

class Vector3D:
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, other):
        return Vector3D(self.a1 + other.a1, self.a2 + other.a2, self.a3 + other.a3)

    def __sub__(self, other):
        return Vector3D(self.a1 - other.a1, self.a2 - other.a2, self.a3 - other.a3)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.a1 * other, self.a2 * other, self.a3 * other)
        elif isinstance(other, Vector3D):
            return self.a1 * other.a1 + self.a2 * other.a2 + self.a3 * other.a3

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normal(self):
        m = self.magnitud()
        return Vector3D(self.a1/m, self.a2/m, self.a3/m)

    def cruz(self, other):
        return Vector3D(
            self.a2 * other.a3 - self.a3 * other.a2,
            self.a3 * other.a1 - self.a1 * other.a3,
            self.a1 * other.a2 - self.a2 * other.a1
        )

    def proyeccion(self, other):
        escalar = (self * other) / (other.magnitud()**2)
        return escalar * other

    def componente(self, other):
        return (self * other) / other.magnitud()

    def es_perpendicular(self, other):
        return (self * other) == 0

    def es_paralelo(self, other):
        c = self.cruz(other)
        return c.a1 == 0 and c.a2 == 0 and c.a3 == 0


a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)

print((a + b).a1, (a + b).a2, (a + b).a3)
print((2 * a).a1, (2 * a).a2, (2 * a).a3)
print(a.magnitud())
n = a.normal()
print(n.a1, n.a2, n.a3)
print(a * b)
c = a.cruz(b)
print(c.a1, c.a2, c.a3)
p = a.proyeccion(b)
print(p.a1, p.a2, p.a3)
print(a.componente(b))
print(a.es_perpendicular(b))
print(a.es_paralelo(b))
