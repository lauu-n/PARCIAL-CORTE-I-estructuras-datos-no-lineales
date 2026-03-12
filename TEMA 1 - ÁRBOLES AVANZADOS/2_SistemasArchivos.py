class Nodo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hijos = []

class SistemaArchivos:
    def __init__(self):
        self.raiz = Nodo("root", "carpeta")

    def agregar(self, padre, nombre, tipo):
        nuevo = Nodo(nombre, tipo)
        padre.hijos.append(nuevo)
        return nuevo

    def buscar(self, nodo, nombre):
        if nodo.nombre == nombre:
            print("Encontrado:", nodo.nombre)
        for hijo in nodo.hijos:
            self.buscar(hijo, nombre)

    def eliminar(self, nodo, nombre):
        for hijo in nodo.hijos:
            if hijo.nombre == nombre:
                nodo.hijos.remove(hijo)
                print("Eliminado:", nombre)
                return
            else:
                self.eliminar(hijo, nombre)

    def mostrar(self, nodo, nivel=0):
        print("  " * nivel + nodo.nombre)
        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)


# PRUEBA
print("PUNTO 2: SISTEMA DE ARCHIVOS")

sistema = SistemaArchivos()

carpeta_docs = sistema.agregar(sistema.raiz, "documentos", "carpeta")
sistema.agregar(carpeta_docs, "notas.txt", "archivo")
sistema.agregar(carpeta_docs, "foto.jpg", "archivo")

print("Contenido del sistema:")
sistema.mostrar(sistema.raiz)

print("Buscar archivo:")
sistema.buscar(sistema.raiz, "foto.jpg")

print("Eliminar archivo:")
sistema.eliminar(sistema.raiz, "notas.txt")

print("Buscar nuevamente:")
sistema.buscar(sistema.raiz, "notas.txt")

"""
ANÁLISIS DE COMPLEJIDAD:
- Agregar: O(1) para agregar un nodo a la lista de hijos.
- Buscar: O(n) en el peor caso, donde n es el número total de nodos, ya que se puede recorrer todo el árbol.
- Eliminar: O(n) en el peor caso, ya que se puede recorrer todo el árbol para encontrar el nodo a eliminar.
- Mostrar: O(n) ya que se recorre todo el árbol para mostrar su contenido.
- En general, las operaciones de búsqueda y eliminación pueden ser costosas en árboles no balanceados o con muchos nodos.
"""