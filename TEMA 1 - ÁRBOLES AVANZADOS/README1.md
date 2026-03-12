# Estructura Organizacional
# Problema: Modelar la jerarquía de una universidad mediante un árbol N-ario.

## 1. Definición: 
Estructura de datos jerárquica donde cada nodo puede tener un número variable de hijos (desde 0 hasta N, donde N puede ser ilimitado). A diferencia de los árboles binarios, no hay límite en la cantidad de descendientes directos.

## 1.1. Características: 
- Raíz: Nodo superior (Rectoría).
- Nodos internos: Tienen al menos un hijo (Facultades, Programas).
- Hojas: Nodos sin hijos (Asignaturas).
- Altura: Número máximo de niveles desde la raíz hasta una hoja.
- Grado: Número máximo de hijos de un nodo.

## 2. Representación en memoria: 
En lenguajes como Python, se representa típicamente con una clase Nodo que contiene: nombre (dato) hijos (lista de referencias a otros nodos).

## 3. Operaciones fundamentales:
- Inserción: Agregar un nuevo nodo como hijo de un nodo existente.
- Recorridos:
    Por niveles (BFS): Se usa una cola para visitar nivel por nivel.
    Profundidad (DFS): Preorden, postorden.
- Cálculo de altura: Máxima profundidad desde la raíz.
- Búsqueda: Encontrar un nodo por nombre.

## 4. Complejidad temporal y espacial:
- Inserción: O(1) si se tiene referencia al padre; O(n) si se busca primero.
- Búsqueda: O(n) en el peor caso (recorrer todo el árbol).
- Recorrido por niveles: O(n) (cada nodo se visita una vez).
- Altura: O(n) si se recorre completo; O(1) si se mantiene actualizada.
- Espacio: O(n) para almacenar n nodos.

## 5. Aplicaciones reales:
- Sistemas de archivos: Carpetas y archivos.
- Jerarquías organizacionales: Empresas, universidades.
- Árboles genealógicos.
- Estructuras de menús en aplicaciones.
- Dependencias de software.

## 6. Análisis comparativo con otras estructuras
| Estructura      | Ventajas                              | Desventajas                               |
| --------------- | ------------------------------------- |------------------------------------------ |
| Árbol N-ario    | Flexible, refleja jerarquías reales   | Búsqueda lineal en hijos                  |
| Árbol binario   | Búsqueda eficiente                    | No modela fácilmente relaciones múltiples |
| Lista de listas | Simple                                | Pérdida de semántica jerárquica           |

```

```