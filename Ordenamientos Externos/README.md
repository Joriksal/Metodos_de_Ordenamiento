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
  straight_merge_sort("unsorted.txt", "sorted.txt", chunk_size=3)