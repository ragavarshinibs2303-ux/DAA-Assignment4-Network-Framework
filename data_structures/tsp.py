class TSPExactSolver:
    """
    Exact combinatorial search for port maintenance tours (Travelling Salesperson Problem).
    Demonstrates NP-Hard scalability limits.
    """
    def __init__(self, cost_matrix):
        self.cost_matrix = cost_matrix
        self.num_nodes = len(cost_matrix)
        self.min_cost = float('inf')
        self.best_tour = []

    def tsp_backtracking(self, curr_node, count, cost, current_tour, visited):
        if count == self.num_nodes and self.cost_matrix[curr_node][0] > 0:
            total_cost = cost + self.cost_matrix[curr_node][0]
            if total_cost < self.min_cost:
                self.min_cost = total_cost
                self.best_tour = current_tour + [0]
            return

        for i in range(self.num_nodes):
            if not visited[i] and self.cost_matrix[curr_node][i] > 0:
                visited[i] = True
                self.tsp_backtracking(i, count + 1, cost + self.cost_matrix[curr_node][i], current_tour + [i], visited)
                visited[i] = False

    def solve(self):
        visited = [False] * self.num_nodes
        visited[0] = True
        self.tsp_backtracking(0, 1, 0, [0], visited)
        return self.min_cost, self.best_tour
