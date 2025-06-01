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