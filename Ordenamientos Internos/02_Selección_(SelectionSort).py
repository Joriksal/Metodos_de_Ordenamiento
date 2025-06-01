def selection_sort(arr):
    """
    Ordena una lista usando Selection Sort.
    
    Parámetros:
    - arr (list): Lista a ordenar (se modifica in-place).
    
    Retorna:
    - None (la lista original es ordenada directamente).
    """
    
    # Recorremos todo el array
    for i in range(len(arr)):
        # Suponemos que el primer elemento no ordenado es el mínimo
        min_idx = i
        
        # Buscamos el índice del elemento más pequeño en la sublista no ordenada
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Actualizamos el índice del mínimo
        
        # Intercambiamos el elemento mínimo con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista_ejemplo = [64, 25, 12, 22, 11]
    
    print("Lista sin ordenar:", lista_ejemplo)
    selection_sort(lista_ejemplo)
    print("Lista ordenada:", lista_ejemplo)