def insertion_sort(arr):
    """
    Ordena una lista usando el algoritmo de Insertion Sort.
    
    Parámetros:
    - arr (list): Lista a ordenar (se modifica in-place).
    
    Retorna:
    - None (la lista original es ordenada directamente).
    """
    
    # Empezamos desde el segundo elemento (índice 1) hasta el final
    for i in range(1, len(arr)):
        # Guardamos el elemento actual para compararlo e insertarlo
        key = arr[i]
        
        # Iniciamos el índice 'j' en el elemento anterior al actual (i-1)
        j = i - 1
        
        # Movemos los elementos mayores que 'key' una posición a la derecha
        # mientras no lleguemos al inicio del array (j >= 0)
        # y el elemento en 'j' sea mayor que 'key'
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Desplazamos el elemento mayor
            j -= 1               # Movemos 'j' hacia la izquierda
        
        # Insertamos 'key' en la posición correcta (j + 1)
        arr[j + 1] = key


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista_ejemplo = [12, 11, 13, 5, 6]
    
    print("Lista sin ordenar:", lista_ejemplo)
    
    # Llamamos a la función para ordenar la lista
    insertion_sort(lista_ejemplo)
    
    print("Lista ordenada:", lista_ejemplo)