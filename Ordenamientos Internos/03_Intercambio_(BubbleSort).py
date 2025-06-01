def bubble_sort(arr):
    """
    Ordena una lista usando Bubble Sort.
    
    Parámetros:
    - arr (list): Lista a ordenar (se modifica in-place).
    
    Retorna:
    - None (la lista original es ordenada directamente).
    """
    
    n = len(arr)
    
    # Recorremos todos los elementos del array
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Compara elementos adyacentes
            if arr[j] > arr[j+1]:
                # Intercambia si están en el orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista sin ordenar:", lista_ejemplo)
    bubble_sort(lista_ejemplo)
    print("Lista ordenada:", lista_ejemplo)