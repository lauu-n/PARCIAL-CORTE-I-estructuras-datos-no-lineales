from collections import deque

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

class Universidad:
    def __init__(self):
        self.raiz = Nodo("Rectoria")

    def insertar(self, padre, nombre):
        nodo_padre = self.buscar(self.raiz, padre)
        if nodo_padre:
            nodo_padre.hijos.append(Nodo(nombre))

    def buscar(self, nodo, nombre):
        if nodo.nombre == nombre:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar(hijo, nombre)
            if encontrado:
                return encontrado
        return None

    def recorrido_niveles(self):
        cola = deque([(self.raiz, 0)])
        while cola:
            nodo, nivel = cola.popleft()
            print("  " * nivel + nodo.nombre)
            for hijo in nodo.hijos:
                cola.append((hijo, nivel + 1))

    def altura(self, nodo):
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(h) for h in nodo.hijos)

    def profundidad(self, nodo, nombre, nivel=0):
        if nodo.nombre == nombre:
            return nivel
        for hijo in nodo.hijos:
            p = self.profundidad(hijo, nombre, nivel+1)
            if p != -1:
                return p
        return -1


# PRUEBA
print("PUNTO 1: ESTRUCTURA ORGANIZACIONAL")

uni = Universidad()

uni.insertar("Rectoria","Facultad Ingenieria")
uni.insertar("Rectoria","Facultad Ciencias")
uni.insertar("Facultad Ingenieria","Programa Sistemas")
uni.insertar("Programa Sistemas","Algoritmos")

print("Recorrido por niveles:")
uni.recorrido_niveles()

print("\nAltura:", uni.altura(uni.raiz))
print("\nProfundidad Algoritmos:", uni.profundidad(uni.raiz,"Algoritmos"))

"""
ANÁLISIS DE COMPLEJIDAD:
- Inserción: Si no tenemos el padre, la búsqueda es O(n). En nuestra implementación, primero buscamos al padre (O(n)) y luego insertamos en O(1). Total: O(n).
- Recorrido por niveles: O(n) (cada nodo se procesa una vez).
- Altura: O(n) (se recorre todo el árbol en el peor caso).
- Profundidad: O(n) (búsqueda lineal).
"""