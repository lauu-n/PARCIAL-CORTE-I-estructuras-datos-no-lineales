class Estudiante:
    def __init__(self, id, nombre, programa):
        self.id = id
        self.nombre = nombre
        self.programa = programa


class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
        self.registros = 0

    def hash(self, id):
        return sum(ord(c) for c in id) % self.tamaño

    def insertar(self, estudiante):
        indice = self.hash(estudiante.id)
        self.tabla[indice].append(estudiante)
        self.registros += 1

    def buscar(self, id):
        indice = self.hash(id)

        for e in self.tabla[indice]:
            if e.id == id:
                return e

        return None

    def eliminar(self, id):
        indice = self.hash(id)

        for i, e in enumerate(self.tabla[indice]):
            if e.id == id:
                self.tabla[indice].pop(i)
                self.registros -= 1
                return True

        return False

    def factor_carga(self):
        return self.registros / self.tamaño

# PRUEBA
hash_estudiantes = TablaHash(5)

# Insertar estudiantes
estudiantes = [
    Estudiante("2021001", "Ana Perez", "Sistemas"),
    Estudiante("2021002", "Carlos Lopez", "Industrial"),
    Estudiante("2021003", "Maraía Gomez", "Matematicas"),
    Estudiante("2021004", "Juan Diaz", "Fisica"),
    Estudiante("2021005", "Laura Vega", "Quimica"),
    Estudiante("2021006", "Pedro Mora", "Sistemas")  # Causará colisión
]

for e in estudiantes:
    hash_estudiantes.insertar(e)

# Buscar
print("\n~ BUSCAR ~")
id_buscar = "2021003"
encontrado = hash_estudiantes.buscar(id_buscar)
if encontrado:
    print(f"Encontrado: {encontrado.nombre} - {encontrado.programa}")

# Eliminar
print("\n~ ELIMINAR ~")
hash_estudiantes.eliminar("2021002")

# Factor de carga
hash_estudiantes.factor_carga()