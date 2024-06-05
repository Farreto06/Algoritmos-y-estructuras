def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Verifica si el hijo izquierdo es mayor que el nodo actual
    if left < n and arr[i] < arr[left]:
        largest = left

    # Verifica si el hijo derecho es mayor que el nodo más grande encontrado hasta ahora
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Si el nodo más grande no es el nodo actual, intercambia y continúa heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar
        heapify(arr, i, 0)

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Arreglo original:", arr)
heap_sort(arr)
print("Arreglo ordenado:", arr)
