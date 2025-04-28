n, m = map(int, input().split())
limite_carretera = [0] * 100 
velocidad_bessie = [0] * 100 

posicion = 0 
for _ in range(n): 
    longitud, limite_velocidad = map(int, input().split()) 
    for i in range(longitud):
        limite_carretera[posicion + i] = limite_velocidad
    posicion += longitud

posicion = 0
for _ in range(m):
    longitud, velocidad = map(int, input().split())
    for i in range(longitud):
        velocidad_bessie[posicion + 1] = velocidad
    posicion += longitud

velocidad_sobre_limite = 0
for i in range(100):
    if velocidad_bessie[i] > limite_carretera[i]:
        velocidad_sobre_limite = max(velocidad_sobre_limite, velocidad_bessie[i] - limite_carretera[i])

print(velocidad_sobre_limite)