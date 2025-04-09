def inssor(list):   #defininimos la funcion y solicita una lista
    for i in range(1, len(list)):   #para i hasta (desde 1(inicio de la lista) hasta la longitud de la lista)
        clave = list[i]     #declaramos una variable para aligerar las cosas
        j = i - 1   #creamos una variable j
        while j >= 0 and list[j] > clave:   #mientras que j >= 0 y que el valor en la posicion de j sea mayor que el valor en posicion i
            list[j + 1] = list[j]       #mover la posicion del valor proximo al anterior
            j -= 1      #le restamos un numero a j
        list[j + 1] = clave     #clave ahora es el valor que movimos
    return list

#prueba
numeros = [5, 2, 6, 78, .2]
ordenados = inssor(numeros)
print("Lista ordenanda:", ordenados)