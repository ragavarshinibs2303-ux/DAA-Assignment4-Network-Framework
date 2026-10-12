import heapq

class DisjointSet:
    """Disjoint Set Union (DSU) data structure with path compression and rank by union."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal_mst(num_nodes, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree.
    Time Complexity: O(E log E) due to edge sorting.
    """
    # Sort edges based on weight
    sorted_edges = sorted(edges, key=lambda item: item[2])
    ds = DisjointSet(num_nodes)
    mst = []
    total_cost = 0

    for u, v, weight in sorted_edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
            if len(mst) == num_nodes - 1:
                break
    return mst, total_cost

def prim_mst(num_nodes, adj_list):
    """
    Prim's Algorithm for Minimum Spanning Tree using a Min-Heap.
    Time Complexity: O(E log V)
    """
    visited = [False] * num_nodes
    min_heap = [(0, 0, -1)]  # (weight, current_node, parent_node)
    mst = []
    total_cost = 0

    while min_heap and len(mst) < num_nodes:
        weight, u, parent = heapq.heappop(min_heap)

        if visited[u]:
            continue
        
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, weight))
            total_cost += weight

        for v, w in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_cost
