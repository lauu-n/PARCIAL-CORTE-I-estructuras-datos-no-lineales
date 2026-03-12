class NodoTrie:
    def __init__(self):
        self.hijos = {}  # Diccionario carácter, NodoTrie
        self.fin_palabra = False

class Autocompletado:
    def __init__(self):
        self.raiz = NodoTrie()
    
    def insertar(self, palabra):
        # Inserta una palabra en el Trie
        actual = self.raiz
        for c in palabra:
            if c not in actual.hijos:
                actual.hijos[c] = NodoTrie()
            actual = actual.hijos[c]
        actual.fin_palabra = True
    
    def buscar_prefijo(self, prefijo):
        # Busca un prefijo y devuelve el nodo donde termina
        actual = self.raiz
        for c in prefijo:
            if c not in actual.hijos:
                return None
            actual = actual.hijos[c]
        return actual
    
    def sugerencias(self, prefijo):
        # Genera sugerencias de autocompletado
        nodo_prefijo = self.buscar_prefijo(prefijo)
        if not nodo_prefijo:
            return []
        
        sugerencias = []
        self._dfs_sugerencias(nodo_prefijo, prefijo, sugerencias)
        return sugerencias
    
    def _dfs_sugerencias(self, nodo, palabra_actual, sugerencias):
        # DFS para encontrar todas las palabras desde un nodo
        if nodo.fin_palabra:
            sugerencias.append(palabra_actual)
        
        for c, hijo in nodo.hijos.items():
            self._dfs_sugerencias(hijo, palabra_actual + c, sugerencias)
    
    def complejidad_O_L(self):
        # Analiza complejidad O(L)
        print("~ ANÁLISIS DE COMPLEJIDAD O(L) ~")
        print("Inserción: O(L) - L es longitud de la palabra")
        print("Búsqueda de prefijo: O(L) - recorre los L caracteres")
        print("Sugerencias: O(L + M) - L del prefijo + M palabras encontradas")
        print("Memoria: O(N * L) en el peor caso, con compartición de prefijos")

# PRUEBA
autocompletar = Autocompletado()

# Insertar palabras
palabras = ["hola", "mundo", "como", "estas", "hola", "holanda", "hotel", "hoyo", "casa", "carro", "perro", "gato"]
for p in palabras:
    autocompletar.insertar(p)

# Buscar prefijos
print("~ AUTOCOMPLETADO ~")
prefijos = ["ho", "ca", "pe"]
for prefijo in prefijos:
    print(f"Sugerencias para '{prefijo}':", 
        autocompletar.sugerencias(prefijo))

print()
autocompletar.complejidad_O_L()