def ord_burbuja(list):  #definimos la funcion en terminos de la lista
    n = len(list)   #hacemos que n sea igual a la longitud de la lista
    for i in range(n):  #para i hasta n
        for j in range(0, n-i-1):   #ahora para j en rango de (desde el primer valor, hasta el valor n-i-1)
            if list[j] > list[j+1]: #si el valor a evaluar es mayor al siguiente valor hacer
                list[j], list[j+1] = list[j+1], list[j] #cambia de posicion los valores antes menciandos (n1,n2 hacia n2,n1)
    return list #regresa la lista

#Prueba
numeros = [5, 3, 8, 4, 1223, 123, 1, 5.2, 12, 5, 9, 2, 0]   #una lista de numeros
ordenados = ord_burbuja(numeros)    #una variable es igual a la funcion con la lista numeros
print("Lista ordenada:", ordenados) #muestra "lista ordenada" y acontinuacion la lista ordenanda