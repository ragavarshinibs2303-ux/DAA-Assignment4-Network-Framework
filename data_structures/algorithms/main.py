import time
import random
from algorithms.mst import kruskal_mst, prim_mst

def generate_graph(num_nodes, density_type='sparse'):
    """
    Generates sparse or dense graphs for port infrastructure testing.
    - Sparse: |E| is small (approx V)
    - Dense: |E| approaches V*(V-1)/2
    """
    edges = []
    adj_list = {i: [] for i in range(num_nodes)}
    
    if density_type == 'sparse':
        # Connect nodes in a ring/line with extra random edges
        for i in range(num_nodes - 1):
            w = random.randint(1, 20)
            edges.append((i, i + 1, w))
            adj_list[i].append((i + 1, w))
            adj_list[i + 1].append((i, w))
        # Add a few extra edges
        extra = num_nodes // 2
        for _ in range(extra):
            u, v = random.sample(range(num_nodes), 2)
            if not any((e[0] == u and e[1] == v) or (e[0] == v and e[1] == u) for e in edges):
                w = random.randint(1, 20)
                edges.append((u, v, w))
                adj_list[u].append((v, w))
                adj_list[v].append((u, w))
                
    elif density_type == 'dense':
        # Connect almost every node to every other node
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                w = random.randint(1, 50)
                edges.append((i, j, w))
                adj_list[i].append((j, w))
                adj_list[j].append((i, w))
                
    return edges, adj_list

def run_assignment_4_module_1():
    print("==================================================")
    print("ASSIGNMENT 4: Adaptive Network Design & Optimization")
    print("Module 1: Prim vs. Kruskal Backbone Analysis")
    print("==================================================")

    # Test cases across different scales and densities
    test_cases = [
        (50, 'sparse'),
        (50, 'dense'),
        (200, 'sparse'),
        (200, 'dense')
    ]

    for nodes, density in test_cases:
        print(f"\n[Test Case] Nodes: {nodes} | Density: {density.upper()}")
        edges, adj_list = generate_graph(nodes, density)
        print(f"Generated Graph -> Edges: {len(edges)}")

        # Measure Kruskal's Performance
        start_time = time.perf_counter()
        k_mst, k_cost = kruskal_mst(nodes, edges)
        k_time = (time.perf_counter() - start_time) * 1000

        # Measure Prim's Performance
        start_time = time.perf_counter()
        p_mst, p_cost = prim_mst(nodes, adj_list)
        p_time = (time.perf_counter() - start_time) * 1000

        print(f"  -> Kruskal Cost: {k_cost} | Execution Time: {k_time:.4f} ms")
        print(f"  -> Prim's Cost:   {p_cost} | Execution Time: {p_time:.4f} ms")
        assert k_cost == p_cost, "Error: MST costs do not match!"
        print("  -> Status: VERIFIED CORRECT (Optimal MST found by both)")

if __name__ == "__main__":
    run_assignment_4_module_1()
from algorithms.shortest_path import floyd_warshall

def run_assignment_4_module_2():
    print("\n==================================================")
    print("Module 2: All-Pairs Cost Analysis (Floyd-Warshall)")
    print("==================================================")

    # Let's define a small network of 4 major port zones / hubs
    INF = float('inf')
    # Indices: 0: Gate Hub, 1: Container Yard A, 2: Berth Terminal, 3: AGV Depot
    port_network = [
        [  0,   3, INF,   7],
        [INF,   0,   2, INF],
        [  5, INF,   0,   1],
        [  2, INF, INF,   0]
    ]

    nodes = len(port_network)
    print("Computing all-pairs shortest paths between port zones...")
    all_pairs_costs = floyd_warshall(nodes, port_network)

    print("\nShortest Cost Matrix:")
    zone_names = ["Gate Hub", "Yard A", "Berth", "AGV Depot"]
    print(f"{'':<12}" + "".join([f"{name:>12}" for name in zone_names]))
    
    for i in range(nodes):
        row_str = f"{zone_names[i]:<12}"
        for j in range(nodes):
            val = all_pairs_costs[i][j]
            row_str += f"{val:12}" if val != INF else f"{'INF':12}"
        print(row_str)

if __name__ == "__main__":
    # You can keep Module 1 call here too
    run_assignment_4_module_2()
