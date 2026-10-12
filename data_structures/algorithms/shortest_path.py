def floyd_warshall(num_nodes, graph_matrix):
    """
    Floyd-Warshall Algorithm for All-Pairs Shortest Paths.
    Time Complexity: O(V^3)
    Space Complexity: O(V^2)
    
    graph_matrix: 2D list where graph_matrix[i][j] is the weight of edge from i to j.
                  Use float('inf') if no direct edge exists, and 0 for i == j.
    """
    # Initialize distance matrix with the input graph matrix
    dist = [row[:] for row in graph_matrix]
    
    # Main DP transitions
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                # Check if path through vertex k provides a shorter route
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist
