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