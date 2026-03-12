class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.significados = {}

class Diccionario:
    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, palabra, idioma, significado):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrie()
            nodo = nodo.hijos[letra]
        if idioma not in nodo.significados:
            nodo.significados[idioma] = []
        nodo.significados[idioma].append(significado)

    def buscar(self, palabra):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                return None
            nodo = nodo.hijos[letra]
        return nodo.significados

    def buscar_prefijo(self, prefijo):
        nodo = self.raiz
        for letra in prefijo:
            if letra not in nodo.hijos:
                return []
            nodo = nodo.hijos[letra]
        resultados = []
        self._dfs(nodo, prefijo, resultados)
        return resultados

    def _dfs(self, nodo, palabra, resultados):
        if nodo.significados:
            resultados.append((palabra, nodo.significados))
        for letra, hijo in nodo.hijos.items():
            self._dfs(hijo, palabra + letra, resultados)

# PRUEBA
diccionario = Diccionario()

# Insertar palabras en diferentes idiomas
diccionario.insertar("casa", "español", "Edificio para habitar")
diccionario.insertar("casa", "portugués", "Edifício para habitar")
diccionario.insertar("casa", "italiano", "Edificio per abitare")
diccionario.insertar("house", "inglés", "Building for living")
diccionario.insertar("casa", "inglés", "House (from Spanish)")
diccionario.insertar("perro", "español", "Animal doméstico")
diccionario.insertar("dog", "inglés", "Domestic animal")
diccionario.insertar("gato", "español", "Felino doméstico")
diccionario.insertar("cat", "inglés", "Domestic feline")

# Buscar palabras
print("~ BUSCAR PALABRA 'casa' ~")
significados = diccionario.buscar("casa")
for idioma, sigs in significados.items():
    print(f"{idioma}: {sigs}")

print("\n~ BUSCAR PALABRA 'dog' ~")
significados = diccionario.buscar("dog")
for idioma, sigs in significados.items():
    print(f"{idioma}: {sigs}")

# Buscar por prefijo
print("\n~ PALABRAS CON PREFIJO 'ca' ~")
resultados = diccionario.buscar_prefijo("ca")
for palabra, sigs in resultados:
    print(f"{palabra}: {sigs}")

# Análisis
diccionario.optimizar_memoria()

"""
El Trie comparte prefijos entre palabras
Esto reduce memoria cuando hay muchas palabras similares
Inserción: O(L)
Búsqueda: O(L)
Prefijo: depende del número de resultados
"""