def promedio(lista):
    return sum(lista) / len(lista)
def desviacion(lista, prom):
    suma = sum((x - prom) ** 2 for x in lista)
    return (suma / (len(lista) - 1)) ** 0.5
entrada = input("Ingrese 10 números separados por espacio: ").split()
numeros = [float(x) for x in entrada]
prom = promedio(numeros)
desv = desviacion(numeros, prom)
print(f"El promedio es {prom:.2f}")
print(f"La desviación estándar es {desv:.5f}")