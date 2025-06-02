import os
import heapq
import random

def generate_runs(input_file, runs_dir, run_size):
    """
    Genera runs ordenados a partir de un archivo de entrada.
    Cada run se guarda como un archivo independiente en runs_dir.
    
    :param input_file: Ruta al archivo con datos desordenados.
    :param runs_dir: Carpeta donde se almacenarán los runs.
    :param run_size: Tamaño de cada run (cantidad de elementos).
    """
    # Crear la carpeta para los runs si no existe
    if not os.path.exists(runs_dir):
        os.makedirs(runs_dir)

    # Leer todos los datos del archivo y convertirlos en una lista de enteros
    with open(input_file, 'r') as f:
        data = list(map(int, f.read().split()))

    total_numbers = len(data)
    run_count = 0  # Contador de archivos de run generados

    # Dividir los datos en chunks (bloques) del tamaño run_size
    for i in range(0, total_numbers, run_size):
        chunk = data[i:i + run_size]
        chunk.sort()  # Ordenar el chunk para que sea un run válido

        # Crear un archivo por cada run
        run_filename = os.path.join(runs_dir, f'run_{run_count}.txt')
        with open(run_filename, 'w') as run_file:
            run_file.write(' '.join(map(str, chunk)))
        run_count += 1

def balanced_multiway_merge(runs_dir, output_file):
    """
    Realiza el Balanced Multiway Merge a partir de los runs ubicados en runs_dir
    y escribe el resultado final ordenado en output_file.
    
    :param runs_dir: Carpeta que contiene los runs ordenados.
    :param output_file: Archivo donde se escribirá el resultado ordenado.
    """
    # Obtener la lista de archivos run_*.txt y ordenarlos alfabéticamente
    run_files = [os.path.join(runs_dir, f) for f in os.listdir(runs_dir) if f.startswith("run_")]
    run_files.sort()

    # Abrir todos los archivos y convertir su contenido en iteradores de enteros
    file_pointers = [open(f, 'r') for f in run_files]
    iterators = [map(int, fp.read().split()) for fp in file_pointers]

    # Heap para llevar el control del menor elemento entre todos los iteradores
    heap = []
    for i, it in enumerate(iterators):
        try:
            value = next(it)  # Obtener el primer valor del run
            heapq.heappush(heap, (value, i, it))  # Insertar en el heap (valor, índice de run, iterador)
        except StopIteration:
            pass  # En caso de que el archivo esté vacío

    # Abrir el archivo de salida para escribir el resultado ordenado
    with open(output_file, 'w') as out:
        result = []

        # Mientras haya elementos en el heap
        while heap:
            val, i, it = heapq.heappop(heap)  # Extraer el menor valor
            result.append(str(val))  # Agregarlo al resultado final

            # Intentar obtener el siguiente valor del mismo iterador
            try:
                next_val = next(it)
                heapq.heappush(heap, (next_val, i, it))  # Insertarlo de nuevo al heap
            except StopIteration:
                pass  # Si ya no hay más elementos, continuar

        # Escribir todos los valores ordenados al archivo
        out.write(' '.join(result))

    # Cerrar todos los archivos abiertos
    for fp in file_pointers:
        fp.close()

if __name__ == "__main__":
    # Ruta del archivo con datos desordenados
    input_file = "Ordenamientos Externos/03_Balanced_Multiway_Merging/unsorted_data.txt"
    # Ruta del archivo donde se guardará el resultado ordenado
    output_file = "Ordenamientos Externos/03_Balanced_Multiway_Merging/sorted_data.txt"
    # Carpeta donde se guardarán los runs
    runs_directory = "Ordenamientos Externos/03_Balanced_Multiway_Merging/runs"
    # Tamaño de cada run (ajustable según la memoria disponible)
    run_size = 5

    # Crear archivo con 20 números aleatorios entre 1 y 100
    with open(input_file, 'w') as f:
        numbers = [random.randint(1, 100) for _ in range(20)]
        f.write(' '.join(map(str, numbers)))

    # Generar los runs desde el archivo de entrada
    generate_runs(input_file, runs_directory, run_size)
    # Realizar la mezcla múltiple balanceada
    balanced_multiway_merge(runs_directory, output_file)

    # Confirmación
    print(f"Archivo ordenado guardado en {output_file}")
