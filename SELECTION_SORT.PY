def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = (
            lista[minimo], lista[i]
        )
    return lista
numeros = [7, 4, 9, 2]
print(selection_sort(numeros))