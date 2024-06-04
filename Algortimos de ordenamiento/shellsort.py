def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicialmente, el gap es la mitad del tamaño del array

    # Continuar reduciendo el gap hasta que sea 0
    while gap > 0:
        # Realizar un ordenamiento por inserción para este gap size
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Mover elementos de arr[0..i-gap] que estén mayores a arr[i]
            # a una posición adelante de su actual posición
            if j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2  # Reducir el gap para la siguiente iteración

    return arr

# Ejemplo de uso
arr = [12, 34, 54, 2, 3]
sorted_arr = shell_sort(arr)
print("Array ordenado:", sorted_arr)