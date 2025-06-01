class NodoArbol:
    """
    Clase que representa un nodo en un árbol binario de búsqueda.
    
    Atributos:
        valor (int): El valor almacenado en el nodo.
        izquierda (NodoArbol): Referencia al hijo izquierdo.
        derecha (NodoArbol): Referencia al hijo derecho.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar_nodo(raiz, valor):
    """
    Inserta un nuevo valor en el árbol binario de búsqueda.
    
    Parámetros:
        raiz (NodoArbol): El nodo raíz del árbol (o subárbol).
        valor (int): El valor a insertar.
    
    Retorno:
        NodoArbol: La raíz del árbol (posiblemente modificada).
    """
    if raiz is None:
        return NodoArbol(valor)
    
    # Insertar en el subárbol izquierdo si el valor es menor
    if valor < raiz.valor:
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    # Insertar en el subárbol derecho si el valor es mayor o igual
    else:
        raiz.derecha = insertar_nodo(raiz.derecha, valor)
    
    return raiz

def inorden_traversal(raiz, resultado):
    """
    Recorrido inorden (izquierda-raíz-derecha) del árbol.
    
    Parámetros:
        raiz (NodoArbol): El nodo raíz del árbol.
        resultado (list): Lista donde se almacenarán los valores ordenados.
    """
    if raiz:
        inorden_traversal(raiz.izquierda, resultado)
        resultado.append(raiz.valor)
        inorden_traversal(raiz.derecha, resultado)

def tree_sort(arr):
    """
    Implementación del algoritmo Tree Sort para ordenar una lista.
    
    Parámetros:
        arr (list): La lista que se desea ordenar.
    
    Retorno:
        list: Una nueva lista con los elementos ordenados.
    """
    # Construimos el árbol binario de búsqueda
    raiz = None
    for valor in arr:
        raiz = insertar_nodo(raiz, valor)
    
    # Realizamos el recorrido inorden para obtener los elementos ordenados
    resultado = []
    inorden_traversal(raiz, resultado)
    
    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo para ordenar
    datos = [7, 6, 8, 5, 3, 9, 2]
    
    print("Lista original:")
    print(datos)
    
    # Ordenamos usando Tree Sort
    datos_ordenados = tree_sort(datos)
    
    print("\nLista ordenada:")
    print(datos_ordenados)