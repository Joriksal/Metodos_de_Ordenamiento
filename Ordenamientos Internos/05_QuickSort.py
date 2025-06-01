def partition(arr, low, high):
    """
    Función auxiliar para QuickSort que selecciona un pivote y particiona el array.
    
    Parámetros:
        arr (list): Lista a ordenar
        low (int): Índice inicial del subarray
        high (int): Índice final del subarray
    
    Retorno:
        int: Índice de la posición final del pivote
    """
    # Seleccionamos el último elemento como pivote
    pivot = arr[high]
    
    # Índice del elemento más pequeño
    i = low - 1
    
    # Recorremos el subarray desde low hasta high-1
    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            # Incrementamos el índice del elemento más pequeño
            i += 1
            # Intercambiamos arr[i] y arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Colocamos el pivote en su posición correcta
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    """
    Implementación del algoritmo QuickSort.
    
    Parámetros:
        arr (list): Lista a ordenar (se modifica in-place)
        low (int): Índice inicial (opcional, para llamadas recursivas)
        high (int): Índice final (opcional, para llamadas recursivas)
    """
    # Inicializamos high si no se proporciona (primera llamada)
    if high is None:
        high = len(arr) - 1
    
    # Verificamos si hay elementos para ordenar
    if low < high:
        # Obtenemos el índice de partición
        pi = partition(arr, low, high)
        
        # Ordenamos recursivamente los elementos antes y después de la partición
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# Ejemplo de uso y demostración
if __name__ == "__main__":
    # Lista de ejemplo para ordenar
    datos = [10, 7, 8, 9, 1, 5, 3, 6, 2, 4]
    
    print("Lista original:")
    print(datos)
    
    # Llamamos a QuickSort
    quick_sort(datos)
    
    print("\nLista ordenada:")
    print(datos)