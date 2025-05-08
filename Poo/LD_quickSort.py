

def quicksort(array):
    if len(array) > 1:
        # Escolhe o pivô (primeiro elemento)
        pivot = array[0]
        
        # Cria subarrays vazios
        subarray1 = []
        subarray2 = []
        
        # Particiona o array (ignora o pivô)
        i = 1
        while i < len(array):
            if array[i] < pivot:
                subarray1.append(array[i])
            else:
                subarray2.append(array[i])
            i += 1
        
        # Ordena os subarrays recursivamente
        quicksort(subarray1)
        quicksort(subarray2)
        
        # Reconstrói o array original ordenado
        j = 0
        # Copia subarray1
        for num in subarray1:
            array[j] = num
            j += 1
        # Adiciona o pivô
        array[j] = pivot
        j += 1
        # Copia subarray2
        for num in subarray2:
            array[j] = num
            j += 1

# Exemplo de uso
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Array original:", arr)
    quicksort(arr)
    print("Array ordenado:", arr)  