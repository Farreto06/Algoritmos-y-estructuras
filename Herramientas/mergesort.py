def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        sorted_list = []
        left_index, right_index = 0, 0

        # Compara elementos de left y right y los ordena
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        # Añade los elementos restantes de left
        sorted_list.extend(left[left_index:])
        # Añade los elementos restantes de right
        sorted_list.extend(right[right_index:])
        
        return sorted_list

    # Divide el arreglo en dos mitades
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Une las dos mitades ordenadas
    return merge(left_half, right_half)

# Ejemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = merge_sort(arr)
print(sorted_arr)
