def quick(list):    #definimos la funcion
    if len(list) <= 1:  #si la longitud de la lista es menor o igual a 1 solo regresala
        return list     #regresa la lista
    else:   #si no
        pivote = list[0]    #definimos un pivote que es de donde cortara el ordenamiento
        menores = [x for x in list[1:] if x <= pivote]  
        mayores = [x for x in list[1:] if x >= pivote]
        return quick(menores) + [pivote] + quick(mayores)

#pruebas
numeros = [4, 5, .2, 9]
ordenados = quick(numeros)
print("Lista ordenana:", ordenados)