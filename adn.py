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
