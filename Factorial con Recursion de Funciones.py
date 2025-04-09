def factorial(n):   #definimos nuestra funcion con n como requisito
    if n == 0 or n == 1:    #si n es 1 o 0
        return 1    #devolver el valor de 1
    return n * factorial(n - 1)     #esta es la parte recursiva se multiplica n por la misma funcion -1

#pruebas
numero = 25
print(f"El factorial de {numero} es {factorial(numero)}")