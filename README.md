# Computación con ADN - Simulación en Python

## Introducción a la Computación con ADN
La computación con ADN es un paradigma de computación no convencional que utiliza moléculas de ADN para realizar cálculos. Fue introducida por Leonard Adleman en 1994 al resolver un problema NP-completo utilizando procesos bioquímicos en un laboratorio. La idea clave detrás de esta tecnología es aprovechar la enorme capacidad de paralelización del ADN, permitiendo la solución de problemas complejos en tiempos relativamente cortos.

### Características Claves de la Computación con ADN
1. **Codificación de Datos**: Se usan las cuatro bases nitrogenadas del ADN (A, C, G, T) para representar información de manera similar a los bits en computación clásica.
2. **Paralelismo Masivo**: Las moléculas de ADN pueden combinarse y replicarse simultáneamente, permitiendo cálculos en paralelo.
3. **Procesamiento Bioquímico**: Se utilizan técnicas de biología molecular como la hibridación, amplificación (PCR) y separación en gel.
4. **Aplicaciones**: Resolución de problemas combinatorios, almacenamiento de información y biocomputación.

## Implementación en Python
Esta implementación en Python simula la solución de un **problema del camino hamiltoniano** en un grafo utilizando principios de computación con ADN.

```python
import itertools
import random

def generate_dna_sequence(length=6):
    """Genera una secuencia de ADN aleatoria de longitud dada."""
    return ''.join(random.choices("ACGT", k=length))

def generate_graph(num_nodes):
    """Genera un grafo representado por nodos con secuencias de ADN."""
    graph = {}
    for i in range(num_nodes):
        graph[i] = generate_dna_sequence()
    return graph

def generate_edges(graph):
    """Genera pares de nodos como conexiones en el grafo (simulando un grafo dirigido)."""
    nodes = list(graph.keys())
    edges = list(itertools.combinations(nodes, 2))  # Generar todas las conexiones posibles
    return random.sample(edges, k=min(len(edges), len(nodes) * 2))  # Seleccionar algunas conexiones

def find_hamiltonian_paths(graph, edges):
    """Encuentra caminos Hamiltonianos en el grafo usando ADN."""
    nodes = list(graph.keys())
    valid_paths = []
    for perm in itertools.permutations(nodes):
        path_edges = [(perm[i], perm[i+1]) for i in range(len(perm)-1)]
        if all(edge in edges for edge in path_edges):
            valid_paths.append(perm)
    return valid_paths

# Generación del grafo y simulación
graph = generate_graph(5)  # 5 nodos
edges = generate_edges(graph)
hamiltonian_paths = find_hamiltonian_paths(graph, edges)

# Mostrar resultados
print("Grafo generado:")
for node, seq in graph.items():
    print(f"Nodo {node}: {seq}")

print("\nConexiones:")
for edge in edges:
    print(f"{edge[0]} -> {edge[1]}")

print("\nCaminos Hamiltonianos encontrados:")
for path in hamiltonian_paths:
    print(" -> ".join(map(str, path)))

```

### Descripción del Código
El código genera un grafo aleatorio en el que:
- Cada nodo es representado por una secuencia de ADN aleatoria.
- Se crean conexiones entre nodos simulando enlaces en el grafo.
- Se buscan caminos Hamiltonianos utilizando combinaciones y permutaciones de nodos.

### Pasos de la Implementación
1. **Generación del Grafo**:
   - Se crean nodos con secuencias de ADN aleatorias.
   - Se establecen conexiones (aristas) entre nodos.
2. **Búsqueda de Caminos Hamiltonianos**:
   - Se generan todas las posibles permutaciones de nodos.
   - Se verifican qué permutaciones respetan las conexiones existentes.
3. **Visualización de Resultados**:
   - Se imprimen los nodos con sus secuencias de ADN.
   - Se muestran las conexiones creadas.
   - Se listan los caminos Hamiltonianos encontrados.

### Requisitos del Entorno
Para ejecutar el código, necesitas:
- Python 3.x
- Librerías estándar de Python (random, itertools)

### Ejecución
Para ejecutar la simulación, simplemente corre el script en un entorno de Python:
```sh
python dna_computation.py
```

### Resultados Esperados
El programa generará un grafo con nodos aleatorios y mostrará los caminos Hamiltonianos encontrados, representando cómo la computación con ADN puede resolver problemas combinatorios.

---

Si deseas mejorar la simulación agregando visualización gráfica o aumentando el número de nodos, puedes modificar los parámetros en la función `generate_graph()` y `generate_edges()`.

¡Esperamos que este proyecto te ayude a entender los principios de la computación con ADN en un entorno digital!
