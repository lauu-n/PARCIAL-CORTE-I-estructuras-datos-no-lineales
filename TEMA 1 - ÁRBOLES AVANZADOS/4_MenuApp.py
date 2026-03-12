class NodoMenu:
    def __init__(self, opcion):
        self.opcion = opcion
        self.subopciones = []  # Hijos del menú

class MenuAplicacion:
    def __init__(self, raiz):
        self.raiz = NodoMenu(raiz)
    
    def agregar_subopcion(self, padre, opcion):
        # Inserta una subopción en el menú
        nodo_padre = self.buscar(self.raiz, padre)
        if nodo_padre:
            nodo_padre.subopciones.append(NodoMenu(opcion))
            return True
        return False
    
    def buscar(self, nodo, opcion):
        # Búsqueda DFS para encontrar una opción
        if nodo.opcion == opcion:
            return nodo
        for sub in nodo.subopciones:
            resultado = self.buscar(sub, opcion)
            if resultado:
                return resultado
        return None
    
    def navegar(self, opcion, ruta=""):
        # Simula navegación mostrando la ruta
        nodo = self.buscar(self.raiz, opcion)
        if nodo:
            ruta_actual = ruta + " > " + nodo.opcion if ruta else nodo.opcion
            print(f"Navegando: {ruta_actual}")
            if nodo.subopciones:
                print("Subopciones disponibles:")
                for sub in nodo.subopciones:
                    print(f"  - {sub.opcion}")
            return ruta_actual
        return None
    
    def contar_por_nivel(self):
        # Cuenta nodos por nivel usando BFS
        from collections import deque
        if not self.raiz:
            return {}
        
        conteo = {}
        cola = deque([(self.raiz, 0)])  # (nodo, nivel)
        
        while cola:
            nodo, nivel = cola.popleft()
            conteo[nivel] = conteo.get(nivel, 0) + 1
            for sub in nodo.subopciones:
                cola.append((sub, nivel + 1))
        
        return conteo
    

# PRUEBA
menu = MenuAplicacion("Sistema Principal")

# Construir menú
menu.agregar_subopcion("Sistema Principal", "Archivo")
menu.agregar_subopcion("Sistema Principal", "Edición")
menu.agregar_subopcion("Sistema Principal", "Ayuda")
menu.agregar_subopcion("Archivo", "Nuevo")
menu.agregar_subopcion("Archivo", "Abrir")
menu.agregar_subopcion("Archivo", "Guardar")
menu.agregar_subopcion("Edición", "Copiar")
menu.agregar_subopcion("Edición", "Pegar")

# Simular navegación
print("~ SIMULACIÓN DE NAVEGACIÓN ~")
menu.navegar("Sistema Principal")
print()
menu.navegar("Archivo")
print()
menu.navegar("Guardar")

# Contar nodos por nivel
print("\n~ CONTEO POR NIVEL ~")
conteo = menu.contar_por_nivel()
for nivel, cantidad in conteo.items():
    print(f"Nivel {nivel}: {cantidad} nodos")


"""
ANÁLISIS DE COMPLEJIDAD:
- Agregar subopción: O(n) en el peor caso para buscar el nodo padre.
- Búsqueda: O(n) en el peor caso (recorre todo el árbol).
- Navegación: O(1) si se tiene el nodo, O(n) si se busca.
- Conteo por nivel: O(n) - recorre todos los nodos una vez.
"""