# HASH
## 1. Definición: 
Estructura de datos que asocia llaves o claves con valores. Utiliza una función hash para calcular un índice (posición) en un arreglo donde se almacena el valor correspondiente. Permite operaciones de inserción, búsqueda y eliminación en tiempo constante promedio O(1).

## 1.1. Características: 
- Función hash: Transforma la clave en un índice dentro de la tabla.
- Colisiones: Ocurren cuando dos claves diferentes generan el mismo índice.
- Factor de carga: Número de elementos / tamaño de la tabla. Indica qué tan llena está.
- Redispersión (Rehashing): Proceso de aumentar el tamaño de la tabla cuando el factor de carga supera un umbral.

## 2. Representación en memoria: 
Arreglo (lista) donde cada posición puede ser:
- Un único elemento (direccionamiento abierto)
- Una lista enlazada (encadenamiento separado)
- Otro tipo de estructura para manejar colisiones
```
# Representación con encadenamiento
tabla = [[] for _ in range(tamaño)]
# Cada bucket es una lista de tuplas (clave, valor)
```

## 3. Operaciones fundamentales:
- Inserción: Calcular hash, ir al bucket, agregar (clave, valor).
- Búsqueda: Calcular hash, buscar en el bucket la clave.
- Eliminación: Calcular hash, remover del bucket.
- Redimensionar: Crear tabla más grande y reinsertar todos los elementos.

## 4. Complejidad temporal y espacial:
| Operación       | Promedio    | Peor caso      |
| --------------- | ----------- |--------------- |
| Inserción       | O(1)        | O(n)           |
| Búsqueda        | O(1)        | O(n)           |
| Eliminación     | O(1)        | O(n)           |
| Espacio         | O(n)        | O(n)           |

## 5. Aplicaciones reales:
- Bases de datos (índices).
- Cachés (memcached, redis).
- Diccionarios en lenguajes de programación.
- Tablas de símbolos en compiladores.
- Routing de redes.

## 6. Análisis comparativo con otras estructuras
| Estructura      | Ventajas                              | Desventajas                        |
| --------------- | ------------------------------------- |----------------------------------- |
| Tabla Hash      | Búsqueda O(1) promedio, flexible      | No ordenada, colisiones            |
| Árbol binario   | Ordenado, operaciones O(log n)        | Más lento que hash en promedio     |
| Lista           | Simple, ordenable                     | Búsqueda O(n)                      |
| Trie            | Búsqueda por prefijo                  | Mayor uso de memoria               |

---

# HEAP
## 1. Definición: 
Árbol binario completo que satisface la propiedad de heap:
- Heap mínimo: El valor de cada nodo es menor o igual que el de sus hijos (raíz = mínimo).
- Heap máximo: El valor de cada nodo es mayor o igual que el de sus hijos (raíz = máximo).

## 1.1. Características: 
- Árbol completo: Todos los niveles están llenos excepto posiblemente el último.
- Representación implícita: Se puede representar en un arreglo sin punteros.
- Relación padre-hijo: Para un nodo en índice i:
    - Hijo izquierdo: 2i + 1
    - Hijo derecho: 2i + 2
    - Padre: (i - 1) // 2

## 2. Representación en memoria: 
Arreglo (lista) donde los elementos se organizan según las relaciones de índice.
```
# Representación de heap mínimo
heap = [1, 3, 2, 7, 5, 4, 6]  # El primer elemento es el mínimo
```

## 3. Operaciones fundamentales:
- Insertar: Agregar al final y "flotar" hacia arriba.
- Extraer mínimo/máximo: Reemplazar raíz con último elemento y "hundir" hacia abajo.
- Ver raíz: Acceder al primer elemento O(1).
- Construir heap: Desde un arreglo desordenado O(n).

## 4. Complejidad temporal y espacial:
| Operación             | Complejidad |
| --------------------- | ----------- |
| Insertar              | O(log n)    |
| Extraer mínimo/máximo | O(log n)    |
| Ver raíz              | O(1)        |
| Construir heap        | O(n)        |
| Espacio               | O(n)        |

## 5. Aplicaciones reales:
- Colas de prioridad (planificadores).
- Algoritmo de Dijkstra (rutas más cortas).
- Ordenamiento (Heapsort).
- Simulación de eventos discretos.
- Selección de los k elementos más grandes/pequeños.

## 6. Análisis comparativo con otras estructuras
| Estructura               | Ventajas                                 | Desventajas             |
| ------------------------ | ---------------------------------------- |------------------------ |
| Heap                     | Extraer mínimo O(log n), inserción rápida| Solo acceso al extremo  |
| Lista ordenada           | Todos los elementos ordenados            | Inserción O(n)          |
| Árbol binario balanceado | Todas las operaciones O(log n)           | Mayor complejidad       |
| Cola simple              | Simple, FIFO                             | No hay prioridades      |

---

# COLA CON PRIORIDAD
## 1. Definición: 
Tipo abstracto de datos donde cada elemento tiene una prioridad asociada. Los elementos con mayor prioridad se extraen antes que los de menor prioridad, independientemente del orden de inserción.

## 1.1. Características: 
- Prioridad: Puede ser numérica (mayor número = mayor prioridad o viceversa).
- Implementación típica: Usando un heap (máximo o mínimo).
- FIFO con prioridad: A igual prioridad, puede mantener orden de llegada.

## 2. Representación en memoria: 
Generalmente implementada con un heap. Cada elemento se almacena como una tupla (prioridad, dato).
```
# Representación en heap (máxima prioridad primero)
cola = [(-prioridad, dato)]  # Negativo para heap mínimo de Python
```

## 3. Operaciones fundamentales:
- Encolar (push): Insertar elemento con su prioridad.
- Desencolar (pop): Extraer el elemento de mayor prioridad.
- Ver frente (peek): Consultar el elemento de mayor prioridad sin extraerlo.
- Cambiar prioridad: Modificar prioridad de un elemento (requiere reorganizar).

## 4. Complejidad temporal y espacial:
| Operación       | Complejidad |
| --------------- | ----------- |
| Encolar         | O(log n)    |
| Desencolar      | O(log n)    |
| Ver frente      | O(1)        |
| Espacio         | O(n)        |

## 5. Aplicaciones reales:
- Planificadores de procesos en sistemas operativos.
- Gestión de paquetes en redes.
- Sistemas de triaje en urgencias médicas.
- Algoritmos de búsqueda (A*, Dijkstra).
- Simulaciones por eventos.

## 6. Análisis comparativo con otras estructuras
| Estructura              | Ventajas                        | Desventajas                    |
| ----------------------- | ------------------------------- |------------------------------- |
| Cola simple             | Simple, orden de llegada        | No hay prioridades             |
| Lista ordenada          | Todos ordenados                 | Inserción lenta O(n)           |
| Árbol balanceado        | Todas operaciones O(log n)      | Mayor overhead                 |
| Cola prioridad (heap)   | Eficiente, prioridades dinámicas| Solo acceso al máximo/mínimo   |