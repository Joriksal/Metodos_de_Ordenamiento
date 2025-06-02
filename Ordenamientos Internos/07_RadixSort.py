def counting_sort(arr, exp):
    """
    Función auxiliar que ordena un array según un dígito específico usando Counting Sort.
    
    Parámetros:
        arr (list): Lista a ordenar
        exp (int): Exponente que representa el dígito actual (1, 10, 100, ...)
    
    Retorno:
        list: Lista ordenada según el dígito actual
    """
    n = len(arr)
    output = [0] * n  # Array de salida
    count = [0] * 10   # Array de conteo (para dígitos 0-9)
    
    # Contamos la frecuencia de cada dígito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Calculamos las posiciones reales en el output
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # Construimos el array de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copiamos el resultado al array original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Implementación del algoritmo Radix Sort para números enteros positivos.
    
    Parámetros:
        arr (list): Lista a ordenar (se modifica in-place)
    """
    # Encontramos el número máximo para saber el número de dígitos
    max_num = max(arr) if arr else 0
    
    # Aplicamos Counting Sort para cada dígito, desde el menos significativo
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Pasamos al siguiente dígito


# Ejemplo de uso y demostración
if __name__ == "__main__":
    # Lista de ejemplo para ordenar
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    
    print("Lista original:")
    print(datos)
    
    # Llamamos a RadixSort
    radix_sort(datos)
    
    print("\nLista ordenada:")
    print(datos)