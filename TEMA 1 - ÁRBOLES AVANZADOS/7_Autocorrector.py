class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.fin = False


class Corrector:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrie()
            nodo = nodo.hijos[letra]
        nodo.fin = True

    def cargar_diccionario(self, palabras):
        for p in palabras:
            self.insertar(p.lower())

    def es_valida(self, palabra):
        nodo = self.raiz
        for letra in palabra.lower():
            if letra not in nodo.hijos:
                return False
            nodo = nodo.hijos[letra]
        return nodo.fin

    def detectar_invalidas(self, texto):
        palabras = texto.split()
        invalidas = []
        for p in palabras:
            if not self.es_valida(p):
                invalidas.append(p)
        return invalidas

    def sugerir(self, palabra):
        sugerencias = []
        for letra in "abcdefghijklmnopqrstuvwxyz":
            candidata = palabra + letra
            if self.es_valida(candidata):
                sugerencias.append(candidata)
        return sugerencias

"""    
COMPARACIÓN CON HASH:
Trie: permite buscar por prefijos
Hash: búsqueda más rápida pero sin prefijos
"""

"""
COMPARACIÓN DE MEMORIA:
Trie usa más memoria por nodos
Hash usa menos memoria
"""