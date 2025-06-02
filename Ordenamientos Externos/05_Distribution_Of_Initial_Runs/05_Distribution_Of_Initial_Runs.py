import os
import random

def generate_runs(input_file, runs_dir, run_size):
    """
    Genera runs ordenados a partir de un archivo de entrada.
    Cada run se guarda como un archivo independiente en runs_dir.
    
    :param input_file: Ruta del archivo de entrada con los datos desordenados.
    :param runs_dir: Carpeta donde se guardarán los archivos con los runs.
    :param run_size: Cantidad de elementos por cada run generado.
    """
    # Crear el directorio donde se guardarán los runs, si no existe
    if not os.path.exists(runs_dir):
        os.makedirs(runs_dir)

    # Leer todos los datos del archivo y convertirlos a enteros
    with open(input_file, 'r') as f:
        data = list(map(int, f.read().split()))

    total_numbers = len(data)  # Total de números leídos
    run_count = 0  # Contador de archivos de run generados

    # Dividir los datos en bloques (chunks) del tamaño run_size
    for i in range(0, total_numbers, run_size):
        chunk = data[i:i + run_size]
        chunk.sort()  # Ordenar el bloque antes de guardarlo como run

        # Crear nombre del archivo run y guardarlo
        run_filename = os.path.join(runs_dir, f'run_{run_count}.txt')
        with open(run_filename, 'w') as run_file:
            run_file.write(' '.join(map(str, chunk)))

        run_count += 1  # Incrementar el contador de runs generados

    print(f"Se generaron {run_count} runs en la carpeta '{runs_dir}'.")

if __name__ == "__main__":
    # Rutas de entrada y salida
    input_file = "Ordenamientos Externos/05_Distribution_of_Initial_Runs/unsorted_data.txt"
    runs_directory = "Ordenamientos Externos/05_Distribution_of_Initial_Runs/runs"
    run_size = 5  # Tamaño de cada bloque o run (puede ajustarse)

    # Generar un archivo con números aleatorios como entrada
    with open(input_file, 'w') as f:
        numbers = [random.randint(1, 100) for _ in range(20)]
        f.write(' '.join(map(str, numbers)))

    # Ejecutar la generación de runs
    generate_runs(input_file, runs_directory, run_size)

    print("""\nEste código no genera el archivo final ordenado (sorted_data.txt) porque forma parte únicamente
de la primera fase del ordenamiento externo, conocida como Distribución de Runs Iniciales.""")
