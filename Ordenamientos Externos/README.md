## Ordenamientos Externos

### 1. Straight Merging 
- **Descripción**:  
  Algoritmo de ordenamiento externo que divide los datos en fragmentos ordenados (runs) y luego los mezcla secuencialmente.  

- **Cómo funciona**:  
  1. **Generación de runs**: Lee fragmentos del archivo, los ordena en memoria y los guarda como runs temporales.  
  2. **Mezcla de runs**: Combina pares de runs ordenados hasta obtener un único archivo ordenado.  

- **Complejidad**:  
  - ⏳ **Tiempo**: O(n log n) en promedio.  
  - 💾 **Espacio**: O(n) (requiere almacenamiento temporal para los runs).  

- **Estable**: ✔️ (mantiene el orden relativo de elementos iguales).  

- **Ejemplo de uso**:  
  ```python
  straight_merge_sort("input_file", "output_file", "chunk_size")

### 2. Natural Merging 

- **Descripción**:  
Algoritmo de ordenamiento externo que aprovecha las secuencias ya ordenadas naturales en los datos.  

- **Cómo funciona**:  
    1. **Detección de runs naturales**: Identifica secuencias ascendentes ya existentes  
    2. **Mezcla iterativa**: Combina pares de runs hasta tener un solo archivo ordenado  

- **Complejidad**:  
⏳ **Tiempo**: O(n log n) (peor caso) | O(n) (si hay pre-ordenamiento)  
💾 **Espacio**: O(n) (almacenamiento temporal)  

- **Estable**: ✔️ (mantiene el orden relativo de elementos iguales).

- **Ejemplo de uso**:  
    ```python
    natural_merge_sort("input_filename", "output_filename")

### 3. Balanced Multiway Merging
- **Descripción**:  
  Algoritmo de ordenamiento externo que mezcla varios "runs" ordenados simultáneamente utilizando una estructura de prioridad (heap). Es eficiente para manejar grandes volúmenes de datos con múltiples archivos temporales.

- **Cómo funciona**:  
  1. **Lectura de runs**: Se abren múltiples archivos que contienen fragmentos ya ordenados.  
  2. **Mezcla balanceada**: Se usa una cola de prioridad (heap) para extraer el menor elemento entre los primeros de cada archivo.  
  3. **Escritura**: Los valores extraídos se escriben secuencialmente en el archivo de salida.

- **Complejidad**:  
  - ⏳ **Tiempo**: O(n log k), donde `n` es el total de elementos y `k` el número de runs.  
  - 💾 **Espacio**: O(k), para mantener los punteros a los runs en memoria.  

- **Estable**: ✔️ (mantiene el orden relativo de elementos iguales si se implementa con cuidado).  

- **Ejemplo de uso**:  
  ```python
  balanced_multiway_merge("carpeta_de_runs", "archivo_salida.txt")

### 4. Polyphase Sort
- **Descripción**:  
  Algoritmo de ordenamiento externo que optimiza la mezcla de múltiples runs utilizando una distribución inicial basada en la secuencia de Fibonacci. Es especialmente eficiente cuando se dispone de un número limitado de archivos de trabajo.

- **Cómo funciona**:  
  1. **Generación de runs**: Se crean runs ordenados y se distribuyen entre los archivos de entrada siguiendo una secuencia específica (por ejemplo, Fibonacci) para optimizar las fases de mezcla.  
  2. **Mezcla polifásica**: En cada fase, se seleccionan N-1 archivos como entrada y 1 como salida. Se realiza la mezcla de los runs, y los roles de los archivos se rotan en la siguiente fase. Este proceso continúa hasta que todos los runs se combinan en un único archivo ordenado.

- **Complejidad**:  
  - ⏳ **Tiempo**: O(n log n) en promedio.  
  - 💾 **Espacio**: O(n) (requiere almacenamiento temporal para los runs y archivos de trabajo).

- **Estable**: ❌ (no garantiza mantener el orden relativo de elementos iguales).

- **Ejemplo de uso**:  
  ```python
  polyphase_merge_sort("ruta/a/runs", "ruta/a/archivo_salida.txt")



