class NodoTrieIntencion:
    def __init__(self):
        self.hijos = {}
        self.fin_palabra = False
        self.intencion = None  # Intención asociada a la palabra

class ClasificadorIntenciones:
    def __init__(self):
        self.raiz = NodoTrieIntencion()
    
    def insertar(self, palabra, intencion):
        # Inserta palabra con su intención asociada
        actual = self.raiz
        for c in palabra.lower():
            if c not in actual.hijos:
                actual.hijos[c] = NodoTrieIntencion()
            actual = actual.hijos[c]
        actual.fin_palabra = True
        actual.intencion = intencion
    
    def clasificar(self, frase):
        # Clasifica la intención de una frase
        palabras = frase.lower().split()
        intenciones_detectadas = {}
        for palabra in palabras:
            intencion = self._buscar_intencion(palabra)
            if intencion:
                intenciones_detectadas[intencion] = intenciones_detectadas.get(intencion, 0) + 1
        if not intenciones_detectadas:
            return "intencion_desconocida"
        # Retornar la intención más frecuente
        return max(intenciones_detectadas, key=intenciones_detectadas.get)
    
    def _buscar_intencion(self, palabra):
        #Busca la intención de una palabra#
        actual = self.raiz
        for c in palabra:
            if c not in actual.hijos:
                return None
            actual = actual.hijos[c]
        return actual.intencion if actual.fin_palabra else None
    
    def simular_respuesta(self, frase):
        # Simula una respuesta basada en la intención
        intencion = self.clasificar(frase)
        respuestas = {
            "saludo": "¡Hola! ¿Cómo puedo ayudarte?",
            "despedida": "¡Hasta luego! Que tengas un buen día",
            "ayuda": "Claro, ¿en qué necesitas ayuda?",
            "compra": "Me interesa saber más sobre tu compra",
            "reclamo": "Lamento el inconveniente, voy a ayudarte",
            "intencion_desconocida": "No estoy seguro de entenderte"
        }
        return respuestas.get(intencion, respuestas["intencion_desconocida"])
    
    def evaluar_precision(self, frases_prueba):
        # Evalúa la precisión con frases de prueba
        aciertos = 0
        print("~ EVALUACIÓN DE PRECISIÓN ~")
        for frase, esperada in frases_prueba:
            obtenida = self.clasificar(frase)
            es_correcto = obtenida == esperada
            if es_correcto:
                aciertos += 1
            print(f"Frase: '{frase}'")
            print(f"  Esperada: {esperada}, Obtenida: {obtenida} ... {'correcto' if es_correcto else '✗'}")
        precision = (aciertos / len(frases_prueba)) * 100
        print(f"\nPrecisión: {precision:.1f}%")
        return precision
    
    def escalar_estructura(self):
        # Análisis de escalabilidad
        print("\n~ ESCALABILIDAD ~")
        print("El Trie escala bien con el número de palabras:")
        print("  - Inserción: O(L) por palabra, independiente del total")
        print("  - Búsqueda: O(L) siempre, sin importar cuántas palabras hay")
        print("  - Memoria: Compartición de prefijos optimiza el espacio")

# PRUEBA
clasificador = ClasificadorIntenciones()

# Insertar palabras con intenciones
clasificador.insertar("hola", "saludo")
clasificador.insertar("buenos", "saludo")
clasificador.insertar("dias", "saludo")
clasificador.insertar("adios", "despedida")
clasificador.insertar("chao", "despedida")
clasificador.insertar("ayuda", "ayuda")
clasificador.insertar("como", "ayuda")
clasificador.insertar("comprar", "compra")
clasificador.insertar("precio", "compra")
clasificador.insertar("queja", "reclamo")
clasificador.insertar("problema", "reclamo")

# Simular respuestas
print("~ SIMULACIÓN DE RESPUESTAS ~")
frases = ["hola como estas", "adios", "quiero comprar algo", "tengo una queja"]
for frase in frases:
    print(f"Usuario: {frase}")
    print(f"Bot: {clasificador.simular_respuesta(frase)}\n")

# Evaluar precisión
frases_prueba = [
    ("hola buenos dias", "saludo"),
    ("chao adios", "despedida"),
    ("necesito ayuda", "ayuda"),
    ("quiero comprar", "compra"),
    ("tengo un problema", "reclamo"),
    ("qué precio tiene", "compra")
]
clasificador.evaluar_precision(frases_prueba)
clasificador.escalar_estructura()