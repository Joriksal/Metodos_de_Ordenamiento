def merge_sort(arr):
    """
    Implementación del algoritmo Merge Sort recursivo.
    
    Parámetros:
        arr (list): Lista a ordenar
    
    Retorno:
        list: Nueva lista con los elementos ordenados
    """
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(arr) <= 1:
        return arr
    
    # Dividimos la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Ordenamos recursivamente cada mitad
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Mezclamos las mitades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Función auxiliar que mezcla dos listas ordenadas en una nueva lista ordenada.
    
    Parámetros:
        left (list): Primera lista ordenada
        right (list): Segunda lista ordenada
    
    Retorno:
        list: Lista resultante de mezclar left y right
    """
    result = []
    i = j = 0
    
    # Recorremos ambas listas y añadimos el elemento menor
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Añadimos los elementos restantes de left (si quedan)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Añadimos los elementos restantes de right (si quedan)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


# Ejemplo de uso y demostración
if __name__ == "__main__":
    # Lista de ejemplo para ordenar
    datos = [38, 27, 43, 3, 9, 82, 10]
    
    print("Lista original:")
    print(datos)
    
    # Llamamos a MergeSort
    datos_ordenados = merge_sort(datos)
    
    print("\nLista ordenada:")
    print(datos_ordenados)