def natural_merge_sort(input_file, output_file):
    """
    Ordena un archivo usando Natural Merge Sort
    :param input_file: Archivo de entrada con los datos a ordenar
    :param output_file: Archivo de salida con los datos ordenados
    """
    # Archivos temporales que podrían usarse en implementaciones más avanzadas
    temp_files = ['temp1.txt', 'temp2.txt']
    
    # Leer todos los datos del archivo de entrada
    with open(input_file, 'r') as f_in:
        # Convertir los datos a una lista de enteros
        data = list(map(int, f_in.read().split()))
    
    # Si no hay datos, terminar la ejecución
    if not data:
        return
    
    runs = []  # Aquí se almacenarán todos los runs naturales encontrados
    current_run = [data[0]]  # Iniciar el primer run con el primer elemento
    
    # Recorrer los datos desde el segundo elemento
    for num in data[1:]:
        # Si el número es mayor o igual al último del run actual, agregarlo al run
        if num >= current_run[-1]:
            current_run.append(num)
        else:
            # Si no, guardar el run actual y comenzar uno nuevo
            runs.append(current_run)
            current_run = [num]
    # No olvidar agregar el último run que quedó
    runs.append(current_run)
    
    # Mientras haya más de un run por mezclar
    while len(runs) > 1:
        new_runs = []  # Aquí se almacenarán los runs mezclados
        
        # Recorrer los runs de dos en dos
        for i in range(0, len(runs), 2):
            # Si hay un run siguiente para mezclar
            if i + 1 < len(runs):
                # Mezclar los dos runs y agregar el resultado
                merged = merge(runs[i], runs[i+1])
                new_runs.append(merged)
            else:
                # Si no hay run siguiente, agregar el run actual sin mezclar
                new_runs.append(runs[i])
        # Actualizar la lista de runs con los nuevos runs mezclados
        runs = new_runs
    
    # Escribir el único run restante (ya ordenado) en el archivo de salida
    with open(output_file, 'w') as f_out:
        # Convertir los números a strings y unirlos con espacios
        f_out.write(' '.join(map(str, runs[0])))

def merge(left, right):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada
    :param left: Lista ordenada izquierda
    :param right: Lista ordenada derecha
    :return: Lista resultante de la mezcla
    """
    result = []  # Lista para el resultado
    i = j = 0  # Índices para recorrer las listas left y right
    
    # Mientras haya elementos en ambas listas
    while i < len(left) and j < len(right):
        # Comparar elementos y agregar el menor
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Agregar los elementos restantes de left (si los hay)
    result.extend(left[i:])
    # Agregar los elementos restantes de right (si los hay)
    result.extend(right[j:])
    
    return result

if __name__ == "__main__":
    # Ruta del archivo con datos desordenados
    input_filename = "Ordenamientos Externos/02_Natural_Merging/unsorted_data.txt"
    # Ruta del archivo de salida para datos ordenados
    output_filename = "Ordenamientos Externos/02_Natural_Merging/sorted_data.txt"
    
    # Crear archivo con datos aleatorios si no existe
    import random
    with open(input_filename, 'w') as f:
        # Generar 20 números aleatorios entre 1 y 100
        numbers = [random.randint(1, 100) for _ in range(20)]
        # Escribir los números separados por espacios
        f.write(' '.join(map(str, numbers)))
 
    # Llamar a la función principal de ordenamiento
    natural_merge_sort(input_filename, output_filename)
    
    # Mensaje de confirmación
    print(f"Archivo ordenado guardado en {output_filename}")