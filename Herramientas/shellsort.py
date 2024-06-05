def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Reduce el gap y aplica ordenamiento de inserción
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Ordena los elementos con el gap actual
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Ejemplo de uso
arr = [12, 34, 54, 2, 3]
print("Arreglo original:", arr)
shell_sort(arr)
print("Arreglo ordenado:", arr)
