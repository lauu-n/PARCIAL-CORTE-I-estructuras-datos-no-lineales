import heapq
import random
import time

class Paquete:
    def __init__(self, id, prioridad, tamaño):
        self.id = id
        self.prioridad = prioridad
        self.tamaño = tamaño
        self.llegada = time.time()

class SimuladorRed:
    def __init__(self):
        self.cola = []
        self.procesados = []

    def recibir_paquete(self, paquete):
        heapq.heappush(self.cola, (-paquete.prioridad, paquete))
        print("Llega paquete", paquete.id, "prioridad", paquete.prioridad)

    def procesar_paquete(self):
        if self.cola:
            prioridad, paquete = heapq.heappop(self.cola)

            time.sleep(0.1)

            paquete.procesado = time.time()
            paquete.espera = paquete.procesado - paquete.llegada

            self.procesados.append(paquete)

            print("Procesado paquete", paquete.id, "prioridad", -prioridad)

    def simular(self, n):
        for i in range(1, n+1):
            p = Paquete(i, random.randint(1,10), random.randint(1,20))
            self.recibir_paquete(p)

        inicio = time.time()

        while self.cola:
            self.procesar_paquete()

        fin = time.time()

        print("\nTiempo total:", fin - inicio)

    def analizar(self):
        esperas = [p.espera for p in self.procesados]

        print("\nAnálisis:")
        print("Paquetes procesados:", len(self.procesados))
        print("Espera promedio:", sum(esperas)/len(esperas))
        print("Espera mínima:", min(esperas))
        print("Espera máxima:", max(esperas))

# PRUEBA

sim = SimuladorRed()
sim.simular(8)
sim.analizar()

"""
ANÁLISIS DE RESULTADOS:
Se calcula:
- espera promedio
- espera mínima
- espera máxima
para evaluar el comportamiento del sistema.
"""