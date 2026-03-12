class NodoModulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dependencias = []  # Módulos de los que depende
        self.dependientes = []   # Módulos que dependen de este

class GestorDependencias:
    def __init__(self):
        self.modulos = {}
    
    def agregar_modulo(self, nombre):
        self.modulos[nombre] = NodoModulo(nombre)
    
    def definir_dependencia(self, modulo, depende_de):
        """modulo depende de depende_de"""
        m = self.modulos[modulo]
        d = self.modulos[depende_de]
        m.dependencias.append(d)
        d.dependientes.append(m)
    
    def construir_arbol(self, nombre_raiz, nivel=0, visitados=None):
        """Construye representación visual del árbol"""
        if visitados is None:
            visitados = set()
        
        if nombre_raiz in visitados:
            return "  " * nivel + f"{nombre_raiz} (ciclo detectado)"
        
        visitados.add(nombre_raiz)
        resultado = "  " * nivel + nombre_raiz + "\n"
        
        for dep in self.modulos[nombre_raiz].dependencias:
            resultado += self.construir_arbol(dep.nombre, nivel + 1, visitados.copy())
        
        return resultado
    
    def impacto_cambio(self, nombre_modulo):
        """Analiza qué módulos se ven afectados si cambia este"""
        afectados = set()
        pila = [self.modulos[nombre_modulo]]
        
        while pila:
            actual = pila.pop()
            for dependiente in actual.dependientes:
                if dependiente.nombre not in afectados:
                    afectados.add(dependiente.nombre)
                    pila.append(dependiente)
        
        return afectados
    
    def evaluar_reutilizacion(self):
        """Evalúa qué módulos son más reutilizados"""
        print("=== ANÁLISIS DE REUTILIZACIÓN ")
        for nombre, modulo in self.modulos.items():
            if len(modulo.dependientes) > 0:
                print(f"{nombre} es usado por {len(modulo.dependientes)} módulo(s)")
        
        # Módulo más reutilizado
        if self.modulos:
            mas_reutilizado = max(self.modulos.values(), 
                                key=lambda m: len(m.dependientes))
            print(f"\nMódulo más reutilizado: {mas_reutilizado.nombre} "
                f"(usado por {len(mas_reutilizado.dependientes)} módulos)")

# PRUEBA
gestor = GestorDependencias()

# Definir módulos
modulos = ["App", "UI", "API", "BaseDatos", "Logger", "Config"]
for m in modulos:
    gestor.agregar_modulo(m)

# Definir dependencias
gestor.definir_dependencia("App", "UI")
gestor.definir_dependencia("App", "API")
gestor.definir_dependencia("API", "BaseDatos")
gestor.definir_dependencia("API", "Logger")
gestor.definir_dependencia("UI", "Logger")
gestor.definir_dependencia("BaseDatos", "Config")
gestor.definir_dependencia("Logger", "Config")

# Construir árbol desde App
print("=== ÁRBOL DE DEPENDENCIAS (desde App) ===")
print(gestor.construir_arbol("App"))

# Analizar impacto
print("\n=== IMPACTO DE CAMBIOS ===")
print("Si cambia 'Config', afecta a:", 
    gestor.impacto_cambio("Config"))
print("Si cambia 'Logger', afecta a:", 
    gestor.impacto_cambio("Logger"))

# Evaluar reutilización
print()
gestor.evaluar_reutilizacion()
