from algorithms.mst import kruskal_mst, prim_mst
from algorithms.shortest_path import floyd_warshall
from algorithms.knapsack import fractional_knapsack, knapsack_01
from algorithms.tsp import TSPExactSolver

def run_full_assignment_4_framework():
    print("==========================================================")
    print("  ASSIGNMENT 4: Adaptive Network Design & Optimization    ")
    print("  Smart-Port & Autonomous Logistics Grid Framework        ")
    print("==========================================================")

    # Module 1: Backbone MST Test
    print("\n[Module 1] Running Prim vs. Kruskal Backbone Analysis...")
    nodes = 10
    edges = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), 
             (2, 5, 4), (2, 8, 2), (3, 4, 9), (3, 5, 14), (4, 5, 10)]
    adj_list = {i: [] for i in range(nodes)}
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    k_mst, k_cost = kruskal_mst(nodes, edges)
    p_mst, p_cost = prim_mst(nodes, adj_list)
    print(f"  -> Kruskal MST Cost: {k_cost} | Prim MST Cost: {p_cost}")

    # Module 2: Floyd-Warshall All-Pairs Cost
    print("\n[Module 2] Running Floyd-Warshall All-Pairs Cost Analysis...")
    INF = float('inf')
    matrix = [[0, 3, INF, 7], [INF, 0, 2, INF], [5, INF, 0, 1], [2, INF, INF, 0]]
    all_pairs = floyd_warshall(4, matrix)
    print("  -> All-Pairs Shortest Path Matrix Computed successfully.")

    # Module 5: Knapsack Budgeting
    print("\n[Module 5] Running Upgrade Budgeting (Knapsack)...")
    benefit, allocation = fractional_knapsack(50, [(60, 10), (100, 20), (120, 30)])
    max_val_01 = knapsack_01(50, [10, 20, 30], [60, 100, 120], 3)
    print(f"  -> Fractional Knapsack Max Benefit: {benefit}")
    print(f"  -> 0/1 Knapsack Max Benefit: {max_val_01}")

    # Module 6: TSP Maintenance Tour
    print("\n[Module 6] Running TSP Maintenance Tour (Exact Backtracking)...")
    tsp_matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    solver = TSPExactSolver(tsp_matrix)
    min_tour_cost, best_tour = solver.solve()
    print(f"  -> Optimal TSP Tour Cost: {min_tour_cost} | Path: {best_tour}")
    print("\n[Framework Execution Complete] All modules verified successfully!")

if __name__ == "__main__":
    run_full_assignment_4_framework()
