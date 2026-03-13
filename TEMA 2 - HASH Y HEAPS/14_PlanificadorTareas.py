import heapq
import time

class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

class Planificador:
    def __init__(self):
        self.heap = []

    def agregar_tarea(self, tarea):
        heapq.heappush(self.heap, (-tarea.prioridad, tarea))

    def ejecutar(self):
        while self.heap:
            prioridad, tarea = heapq.heappop(self.heap)
            print("Ejecutando:", tarea.nombre, "| prioridad:", -prioridad)
            time.sleep(0.2)

# PRUEBA

plan = Planificador()

plan.agregar_tarea(Tarea("Actualizar sistema",5))
plan.agregar_tarea(Tarea("Respaldar datos",3))
plan.agregar_tarea(Tarea("Parche seguridad",10))
plan.agregar_tarea(Tarea("Limpiar cache",1))

plan.ejecutar()

"""
EVALUAR JUSTICIA:
- Ventaja: El heap  que las tareas críticas se ejecutan primero.
- Desventaja: Su uso puede postergar tareas de baja prioridad indefinidamente.
"""