import os
import random

def straight_merge_sort(input_file, output_file, chunk_size=3):
    """
    Implementación del algoritmo Straight Merging (Mezcla Directa) para ordenamiento externo.
    
    Este algoritmo ordena archivos grandes que no caben en memoria dividiéndolos en fragmentos,
    ordenando cada fragmento en memoria y luego mezclándolos progresivamente.
    
    Parámetros:
        input_file (str): Ruta absoluta o relativa del archivo de entrada con datos desordenados.
                         Ejemplo: "data/entrada.txt" o "C:/ordenamiento/unsorted.txt"
        output_file (str): Ruta donde se guardará el archivo ordenado.
        chunk_size (int): Cantidad de elementos a cargar en memoria por cada fragmento (run).
                         Por defecto: 3 (para demostración, en práctica usar valores mayores).
    """
    
    # Fase 1: Generar runs (fragmentos ordenados)
    def generate_runs(file_path, chunk_size):
        """
        Lee el archivo de entrada y genera fragmentos ordenados (runs) en memoria.
        
        Args:
            file_path (str): Ruta del archivo a procesar.
            chunk_size (int): Máximo de elementos por fragmento.
            
        Returns:
            list: Lista de runs (cada run es una lista ordenada de números).
        """
        runs = []  # Aquí almacenaremos todos los fragmentos ordenados
        with open(file_path, 'r') as file:
            while True:
                chunk = []
                # Leemos 'chunk_size' elementos del archivo
                for _ in range(chunk_size):
                    line = file.readline()
                    if not line:  # Fin del archivo
                        break
                    # Convertimos a entero y añadimos al chunk actual
                    chunk.append(int(line.strip()))
                
                if not chunk:  # Si no se leyeron datos, terminamos
                    break
                
                # Ordenamos el chunk en memoria
                chunk.sort()
                # Guardamos este fragmento ordenado
                runs.append(chunk)
        return runs
    
    # Fase 2: Mezclar runs en un archivo ordenado
    def merge_runs(runs, output_path):
        """
        Mezcla progresivamente los fragmentos hasta obtener un único archivo ordenado.
        
        Args:
            runs (list): Lista de fragmentos ordenados a mezclar.
            output_path (str): Ruta donde se guardará el resultado final.
        """
        with open(output_path, 'w') as out_file:
            # Mientras tengamos más de un fragmento, seguimos mezclando
            while len(runs) > 1:
                new_runs = []  # Aquí guardaremos los nuevos fragmentos mezclados
                
                # Procesamos los fragmentos de dos en dos
                for i in range(0, len(runs), 2):
                    if i + 1 < len(runs):  # Si tenemos par de fragmentos
                        # Mezclamos los dos fragmentos ordenados
                        merged = merge_two_sorted_lists(runs[i], runs[i + 1])
                        new_runs.append(merged)
                    else:  # Si queda un fragmento sin pareja
                        new_runs.append(runs[i])  # Lo pasamos directamente
                
                runs = new_runs  # Actualizamos con los nuevos fragmentos mezclados
            
            # Al final solo queda un fragmento completamente ordenado
            # Lo escribimos al archivo de salida
            for num in runs[0]:
                out_file.write(f"{num}\n")
    
    def merge_two_sorted_lists(list1, list2):
        """
        Mezcla dos listas ordenadas en una nueva lista ordenada.
        
        Args:
            list1 (list): Primera lista ordenada.
            list2 (list): Segunda lista ordenada.
            
        Returns:
            list: Lista resultante de mezclar ambas listas ordenadamente.
        """
        merged = []
        i = j = 0  # Índices para recorrer ambas listas
        
        # Recorremos ambas listas simultáneamente
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Añadimos los elementos restantes de la lista no vacía
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        
        return merged
    
    # --- Ejecución principal del algoritmo ---
    # 1. Generamos los fragmentos ordenados (runs) del archivo de entrada
    runs = generate_runs(input_file, chunk_size)
    
    # 2. Mezclamos progresivamente los fragmentos hasta obtener el archivo ordenado
    merge_runs(runs, output_file)


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración de rutas (¡personaliza estas rutas!)
    input_file = "Ordenamientos Externos/01_Straight_Merging/unsorted_data.txt"
    output_file = "Ordenamientos Externos/01_Straight_Merging/sorted_data.txt"
    
    # Crear directorios si no existen
    os.makedirs(os.path.dirname(input_file), exist_ok=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Generar archivo de prueba con números aleatorios si no existe
    if not os.path.exists(input_file):
        print(f"Generando archivo de entrada en: {input_file}")
        with open(input_file, 'w') as f:
            for _ in range(20):  # Generamos 20 números aleatorios
                f.write(f"{random.randint(1, 100)}\n")
    
    print("\nIniciando proceso de ordenamiento...")
    print(f"Archivo de entrada: {input_file}")
    print(f"Archivo de salida: {output_file}")
    
    # Ejecutar el algoritmo
    straight_merge_sort(input_file, output_file)
    
    print("\n¡Ordenamiento completado con éxito!")
    print(f"Resultados guardados en: {output_file}")