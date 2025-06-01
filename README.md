# Metodos de Ordenamiento

### ¿Que es ordenamiento?
Es la operación de arreglar los elementos en algún orden secuencial de acuerdo a un criterio de 
ordenamiento. 
El propósito principal de un ordenamiento es el de facilitar las búsquedas de los miembros del 
conjunto ordenado. 
Ordenar un grupo de datos significa mover los datos o sus referencias para que queden en una 
secuencia por categorías y en forma ascendente o descendente.

### ¿Cuándo conviene usar un método de ordenamiento?
Cuando se requiere hacer una cantidad considerable de búsquedas y es importante el factor tiempo.

### Tipos de ordenamiento:
- **Ordenamiento internos**:
Son aquellos en los que los valores a ordenar están en memoria principal, por lo que se asume  que el tiempo que se requiere para acceder cualquier elemento sea el mismo (a [1], a [500], etc.).

- **Ordenamiento externos**:
Son aquellos en los que los valores a ordenar están en memoria secundaria (disco, cinta, cilindro magnético, etc.), por lo que se asume que el tiempo que se requiere para acceder a cualquier elemento depende de la última posición accesada (posición 1, posición 500, etc.).

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