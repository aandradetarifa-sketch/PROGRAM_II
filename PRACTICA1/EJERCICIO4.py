class Estadistica:
    def __init__(self, lista):
        self._datos = lista.copy()
    @property
    def datos(self):
        return self._datos.copy()
    @datos.setter
    def datos(self, nueva_lista):
        self._datos = nueva_lista.copy()
    def promedio(self):
        if not self._datos:
            return 0
        return sum(self._datos) / len(self._datos)
    def desviacion(self):
        if len(self._datos) < 2:
            return 0
        prom = self.promedio()
        suma = sum((x - prom) ** 2 for x in self._datos)
        return (suma / (len(self._datos) - 1)) ** 0.5

entrada = input("Ingrese 10 números separados por espacio: ").split()
numeros = [float(x) for x in entrada]

est = Estadistica(numeros)
print(f"El promedio es {est.promedio():.2f}")
print(f"La desviación estándar es {est.desviacion():.5f}")