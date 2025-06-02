## Ordenamientos Internos

### 1. Inserción (Insertion Sort)
- **Descripción**:  
  Ordena construyendo una sublista ordenada uno a la vez, insertando cada elemento en su posición correcta dentro de la sublista. Ideal para datos pequeños o parcialmente ordenados.

- **Cómo funciona**:  
  1. Divide la lista en una parte ordenada y otra sin ordenar.  
  2. Toma el primer elemento de la parte sin ordenar y lo inserta en la posición correcta dentro de la parte ordenada.  
  3. Repite hasta que no queden elementos sin ordenar.

- **Complejidad**:  
  - ⏳ **Peor caso**: O(n²) (lista en orden inverso).  
  - ✅ **Mejor caso**: O(n) (lista ya ordenada).  
  - 💾 **Espacio**: O(1) (ordenamiento in-place).

- **Estable**: ✔️ (no cambia el orden relativo de elementos iguales).

- **Ejemplo**:
  ```python
  arr = [12, 11, 13, 5, 6]
  insertion_sort(arr)  # Salida: [5, 6, 11, 12, 13]

### 2. Selección (Selection Sort)
- **Descripción**:  
  Ordena seleccionando repetidamente el elemento más pequeño de la sublista no ordenada y colocándolo al inicio.

- **Cómo funciona**:  
  1. Divide la lista en una parte ordenada (izquierda) y otra no ordenada (derecha).  
  2. Encuentra el elemento mínimo en la sublista no ordenada.  
  3. Intercámbialo con el primer elemento no ordenado.  

- **Complejidad**:  
  - ⏳ **Peor caso**: O(n²) (lista en orden inverso).  
  - ✅ **Mejor caso**: O(n²) (incluso si ya está ordenado).  
  - 💾 **Espacio**: O(1) (ordenamiento in-place).  

- **Estable**: ❌ (puede invertir el orden de elementos iguales al intercambiar).  

- **Ejemplo**:  
  ```python
  arr = [64, 25, 12, 22, 11]
  selection_sort(arr)  # Salida: [11, 12, 22, 25, 64]

### 3. Intercambio (Bubble Sort)
- **Descripción**:  
  Ordena comparando e intercambiando pares de elementos adyacentes hasta que la lista esté ordenada.

- **Cómo funciona**:  
  1. Recorre la lista comparando elementos adyacentes.  
  2. Si están en el orden incorrecto, los intercambia.  
  3. Repite el proceso hasta que no se necesiten más intercambios.  

- **Complejidad**:  
  - ⏳ **Peor caso**: O(n²) (lista en orden inverso).  
  - ✅ **Mejor caso**: O(n) (lista ya ordenada).  
  - 💾 **Espacio**: O(1) (ordenamiento in-place).  

- **Estable**: ✔️ (no cambia el orden relativo de elementos iguales).  

- **Ejemplo**:  
  ```python
  arr = [64, 34, 25, 12, 22, 11, 90]
  bubble_sort(arr)  # Salida: [11, 12, 22, 25, 34, 64, 90]

### 4. Árbol (Tree Sort)
- **Descripción**:  
  Ordena elementos construyendo un árbol binario de búsqueda y luego recorriéndolo en orden (inorden).

- **Cómo funciona**:  
  1. Construye un árbol binario de búsqueda con los elementos de la lista.  
  2. Realiza un recorrido inorden (izquierda-raíz-derecha) del árbol.  
  3. Los elementos se recogen en orden durante el recorrido.  

- **Complejidad**:  
  - ⏳ **Peor caso**: O(n²) (árbol degenerado, como una lista enlazada).  
  - ✅ **Mejor caso**: O(n log n) (árbol balanceado).  
  - 💾 **Espacio**: O(n) (necesita almacenar la estructura del árbol).  

- **Estable**: ✔️ (mantiene el orden relativo de elementos iguales).  

- **Ejemplo**:  
  ```python
  arr = [7, 6, 8, 5, 3]
  tree_sort(arr)  # Salida: [3, 5, 6, 7, 8]

### 5. QuickSort
- **Descripción**:  
  Algoritmo de divide y vencerás que selecciona un "pivote" y particiona el array alrededor de este.

- **Cómo funciona**:  
  1. **Selección de pivote**: Escoge un elemento como pivote (aquí usamos el último elemento).  
  2. **Partición**: Reordena el array colocando menores que el pivote a su izquierda y mayores a su derecha.  
  3. **Recursión**: Aplica el mismo proceso a los subarrays izquierdo y derecho del pivote.  

- **Complejidad**:  
  - ⏳ **Peor caso**: O(n²) (cuando el pivote es el menor/mayor elemento).  
  - ✅ **Mejor caso**: O(n log n) (particiones balanceadas).  
  - 💾 **Espacio**: O(log n) (por la pila de llamadas recursivas).  

- **Estable**: ❌ (no mantiene el orden relativo de elementos iguales).  

- **Ejemplo**:  
  ```python
  arr = [10, 7, 8, 9, 1, 5]
  quick_sort(arr)  # Salida: [1, 5, 7, 8, 9, 10]

### 6. MergeSort
- **Descripción**:  
  Algoritmo de divide y vencerás que divide la lista en mitades, las ordena recursivamente y luego las mezcla.

- **Cómo funciona**:  
  1. **Divide**: Divide la lista desordenada en dos sublistas de aproximadamente igual tamaño.  
  2. **Conquista**: Ordena cada sublista recursivamente aplicando MergeSort.  
  3. **Combina**: Mezcla las dos sublistas ordenadas para producir la solución.  

- **Complejidad**:  
  - ⏳ **Peor caso**: O(n log n)  
  - ✅ **Mejor caso**: O(n log n)  
  - 💾 **Espacio**: O(n) (necesita espacio adicional para mezclar)  

- **Estable**: ✔️ (mantiene el orden relativo de elementos iguales).  

- **Ejemplo**:  
  ```python
  arr = [38, 27, 43, 3, 9, 82]
  merge_sort(arr)  # Salida: [3, 9, 27, 38, 43, 82]

### 7. RadixSort 
- **Descripción**:  
  Algoritmo de ordenamiento no comparativo que procesa dígitos individuales desde el menos significativo (LSD) al más significativo (MSD).

- **Cómo funciona**:  
  1. **Identifica el máximo**: Determina el número con más dígitos.  
  2. **Ordena por dígitos**: Desde la unidad (derecha) hacia la izquierda.  
  3. **Usa Counting Sort**: Para ordenar los números según cada dígito.  

- **Complejidad**:  
  - ⏳ **Peor caso**: O(nk) donde k es el número de dígitos del máximo.  
  - ✅ **Mejor caso**: O(nk)  
  - 💾 **Espacio**: O(n + k)  

- **Estable**: ✔️ (mantiene el orden relativo de elementos iguales).  

- **Ejemplo**:  
  ```python
  arr = [170, 45, 75, 90, 802, 24, 2]
  radix_sort(arr)  # Salida: [2, 24, 45, 75, 90, 170, 802]