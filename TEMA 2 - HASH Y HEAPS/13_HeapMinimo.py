class HeapMinimo:
    def __init__(self):
        self.elementos = []
    
    def insertar(self, valor):
        #Inserta un elemento y reorganiza el heap#
        self.elementos.append(valor)
        self._flotar(len(self.elementos) - 1)
        print(f"Insertado: {valor}")
    
    def _flotar(self, indice):
        #Flota el elemento en índice hacia arriba para mantener heap#
        while indice > 0:
            padre = (indice - 1) // 2
            if self.elementos[indice] < self.elementos[padre]:
                self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
                indice = padre
            else:
                break
    
    def extraer_minimo(self):
        #Extrae y retorna el mínimo elemento#
        if not self.elementos:
            return None
        
        if len(self.elementos) == 1:
            return self.elementos.pop()
        
        minimo = self.elementos[0]
        self.elementos[0] = self.elementos.pop()
        self._hundir(0)
        
        return minimo
    
    def _hundir(self, indice):
        #Hunde el elemento en índice hacia abajo para mantener heap#
        n = len(self.elementos)
        while True:
            menor = indice
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            
            if izquierdo < n and self.elementos[izquierdo] < self.elementos[menor]:
                menor = izquierdo
            if derecho < n and self.elementos[derecho] < self.elementos[menor]:
                menor = derecho
            
            if menor != indice:
                self.elementos[indice], self.elementos[menor] = self.elementos[menor], self.elementos[indice]
                indice = menor
            else:
                break
    
    def ver_minimo(self):
        #Retorna el mínimo sin extraerlo#
        return self.elementos[0] if self.elementos else None
    
    def analizar_O_logn(self):
        #Analiza la complejidad O(log n)
        n = len(self.elementos)
        print("\n~ ANÁLISIS COMPLEJIDAD O(log n) ~")
        print(f"Heap con {n} elementos")
        print(f"Altura del heap: ~{n.bit_length()}")
        print("\nOperaciones:")
        print("- Insertar: O(log n) - flotar desde hoja hasta raíz")
        print("- Extraer mínimo: O(log n) - hundir desde raíz hasta hoja")
        print("- Ver mínimo: O(1) - acceso directo a raíz")
        print("\nDemostración:")
        print(f"  log2({n}) ≈ {n.bit_length() - 1} pasos en el peor caso")
    
    def probar_casos_limite(self):
        # Prueba casos límite#
        print("\n~ PRUEBA CASOS LÍMITE ~")
        
        # Heap vacío
        heap_vacio = HeapMinimo()
        print("Heap vacío - extraer mínimo:", heap_vacio.extraer_minimo())
        
        # Un elemento
        heap_vacio.insertar(42)
        print("Un elemento - mínimo:", heap_vacio.ver_minimo())
        print("Extraer único:", heap_vacio.extraer_minimo())
        
        # Elementos repetidos
        heap_repetidos = HeapMinimo()
        for v in [5, 3, 5, 2, 3, 1]:
            heap_repetidos.insertar(v)
        print("\nHeap con repetidos:", heap_repetidos.elementos)
        while heap_repetidos.elementos:
            print(f"  Extraído: {heap_repetidos.extraer_minimo()}")
        
        # Orden descendente
        heap_desc = HeapMinimo()
        for v in [10, 9, 8, 7, 6]:
            heap_desc.insertar(v)
        print("\nHeap insertado en orden descendente:", heap_desc.elementos)

# PRUEBA
heap = HeapMinimo()

# Insertar elementos
elementos = [5, 3, 8, 1, 9, 2, 7]
print("~ INSERTANDO ELEMENTOS ~")
for e in elementos:
    heap.insertar(e)
print("Heap final:", heap.elementos)

# Extraer mínimo
print("\n~ EXTRACCIÓN DE MÍNIMOS ~")
for _ in range(3):
    minimo = heap.extraer_minimo()
    print(f"Extraído mínimo: {minimo}")
    print(f"Heap restante: {heap.elementos}")

# Análisis complejidad
heap.analizar_O_logn()

# Casos límite
heap.probar_casos_limite()