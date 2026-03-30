import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

    def suma(self, v):
        return AlgebraVectorial(self.x + v.x, self.y + v.y)

    def resta(self, v):
        return AlgebraVectorial(self.x - v.x, self.y - v.y)

    def producto_punto(self, v):
        return self.x * v.x + self.y * v.y

    def producto_cruz(self, v):
        return self.x * v.y - self.y * v.x

    def perpendicular(self, v):
        return self.producto_punto(v) == 0

    def perpendicular_suma_resta(self, v):
        return abs(self.suma(v).magnitud() - self.resta(v).magnitud()) < 1e-9

    def perpendicular_identidad(self, v):
        return abs(self.suma(v).magnitud()**2 - (self.magnitud()**2 + v.magnitud()**2)) < 1e-9

    def paralela(self, v):
        return self.producto_cruz(v) == 0

    def proyeccion_sobre(self, v):
        escalar = self.producto_punto(v) / (v.magnitud()**2)
        return AlgebraVectorial(escalar * v.x, escalar * v.y)

    def componente_en(self, v):
        return self.producto_punto(v) / v.magnitud()


a = AlgebraVectorial(3, 4)
b = AlgebraVectorial(4, -3)

print(a.perpendicular(b))
print(a.paralela(b))
p = a.proyeccion_sobre(b)
print(p.x, p.y)
print(a.componente_en(b))
