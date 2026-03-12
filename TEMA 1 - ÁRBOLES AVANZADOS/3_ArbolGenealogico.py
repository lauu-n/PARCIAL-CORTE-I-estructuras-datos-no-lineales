class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.padres = [] # Relación de dos padres
        self.hijos = [] # Relación de múltiples hijos

class ArbolGenealogico:
    def __init__(self):
        self.personas = {} # Diccionario para acceso rápido por nombre

    def agregar_persona(self, nombre):
        self.personas[nombre] = Nodo(nombre)

    def relacion(self, padre, hijo):
        p = self.personas[padre]
        h = self.personas[hijo]
        h.padres.append(p) # Relación de dos padres
        p.hijos.append(h) # Relación de múltiples hijos

    def ancestros(self, nombre):
        visitados = set()
        pila = [self.personas[nombre]]
        while pila:
            actual = pila.pop() # DFS para encontrar ancestros
            for padre in actual.padres:
                if padre.nombre not in visitados:
                    visitados.add(padre.nombre)
                    pila.append(padre)
        return visitados

    def ancestro_comun(self, p1, p2):
        a1 = self.ancestros(p1)
        a2 = self.ancestros(p2)
        for a in a1:
            if a in a2:
                return a
        return None

    def generaciones(self, nombre):
        nodo = self.personas[nombre]
        if not nodo.padres:
            return 0
        return 1 + max(self.generaciones(p.nombre) for p in nodo.padres)

    def grado_arbol(self):
        max_hijos = 0
        for p in self.personas.values():
            max_hijos = max(max_hijos, len(p.hijos))
        return max_hijos

    def mostrar(self, nodo, nivel=0):
        print("  " * nivel + nodo.nombre)
        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)


# PRUEBA
familia = ArbolGenealogico()

familia.agregar_persona("Juan")
familia.agregar_persona("Maria")
familia.agregar_persona("Carlos")
familia.agregar_persona("Ana")
familia.agregar_persona("Pedro")

familia.relacion("Juan", "Carlos")
familia.relacion("Maria", "Carlos")
familia.relacion("Carlos", "Pedro")

familia.mostrar(familia.personas["Juan"]) # Mostrar desde un ancestro

print("Ancestro comun:", familia.ancestro_comun("Pedro", "Carlos"))
print("Generaciones desde Pedro:", familia.generaciones("Pedro"))
print("Grado del arbol:", familia.grado_arbol())