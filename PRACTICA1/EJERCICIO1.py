import time
import random
class Cronometro:
    def __init__(self):
        self._inicia = int(time.time() * 1000)
        self._finaliza = 0
    @property
    def inicia(self):
        return self._inicia
    @property
    def finaliza(self):
        return self._finaliza
    def iniciar(self):
        self._inicia = int(time.time() * 1000)
        self._finaliza = 0
    def detener(self):
        self._finaliza = int(time.time() * 1000)
    def lapsoDeTiempo(self):
        if self._finaliza == 0:
            return 0
        return self._finaliza - self._inicia
    
def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

tamaño = 100000
numeros = [random.randint(1, 1000000) for _ in range(tamaño)]
print(f"Ordenando {tamaño} números...")
crono = Cronometro()
crono.iniciar()
ordenamiento_seleccion(numeros.copy())
crono.detener()
print(f"Tiempo de ordenación: {crono.lapsoDeTiempo()} ms")