import time
import tracemalloc

class Trie:
    def __init__(self):
        self.raiz = {}

    def insertar(self, palabra, valor):
        nodo = self.raiz
        for c in palabra:
            nodo = nodo.setdefault(c, {})
        nodo["fin"] = valor

    def buscar(self, palabra):
        nodo = self.raiz
        for c in palabra:
            if c not in nodo:
                return None
            nodo = nodo[c]
        return nodo.get("fin")
    
    tracemalloc.start()

class Hash:
    def __init__(self, tamaño=100):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]

    def hash(self, clave):
        return sum(ord(c) for c in clave) % self.tamaño

    def insertar(self, clave, valor):
        i = self.hash(clave)
        self.tabla[i].append((clave, valor))

    def buscar(self, clave):
        i = self.hash(clave)
        for c, v in self.tabla[i]:
            if c == clave:
                return v
        return None
    
hash_t = Hash()
trie_t = Trie()

palabras = ["hola","mundo","perro","gato","casa"]

for p in palabras:
    hash_t.insertar(p, p)
    trie_t.insertar(p, p)

    inicio = time.time()
    hash_t.buscar("perro")
    print("Tiempo Hash:", time.time() - inicio)


    inicio = time.time()
    trie_t.buscar("perro")
    print("Tiempo Trie:", time.time() - inicio)

# Medición de memoria HASH
tracemalloc.start()
hash_t = Hash()
for p in palabras:
    hash_t.insertar(p,p)
mem_hash = tracemalloc.get_traced_memory()[0]
tracemalloc.stop()

# Medición de memoria TRIE
tracemalloc.start()
trie_t = Trie()
for p in palabras:
    trie_t.insertar(p,p)
mem_trie = tracemalloc.get_traced_memory()[0]
tracemalloc.stop()

print("Memoria Hash:", mem_hash/1024, "KB")
print("Memoria Trie:", mem_trie/1024, "KB")

"""
CONCLUSIONES USO ÓPTIMO:

USAR HASH CUANDO:
- Búsquedas exactas son la operación principal")
- La memoria es limitada (menor overhead por elemento)")
- El orden de las claves no importa")
- Se necesita O(1) promedio en búsquedas")

USAR TRIE CUANDO:
- Se necesitan búsquedas por prefijo (autocompletado)
- Hay muchas claves con prefijos comunes
- Se requiere tiempo de búsqueda predecible O(L)
- Las claves son strings y se comparten prefijos

- Hash: +Rápido en búsquedas exactas, -No soporta prefijos")
- Trie: +Soporta prefijos, -Mayor uso de memoria
"""