def fractional_knapsack(capacity, items):
    """
    Greedy approach for divisible network/software upgrades.
    items: list of tuples (benefit, weight)
    """
    # Sort items by value-to-weight ratio in descending order
    graded_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    total_benefit = 0.0
    current_capacity = capacity
    allocation = []

    for benefit, weight in graded_items:
        if current_capacity >= weight:
            current_capacity -= weight
            total_benefit += benefit
            allocation.append((benefit, weight, 1.0)) # 1.0 means fully taken
        else:
            fraction = current_capacity / weight
            total_benefit += benefit * fraction
            allocation.append((benefit, weight, fraction))
            break
            
    return total_benefit, allocation

def knapsack_01(capacity, weights, values, n):
    """
    Dynamic Programming approach for indivisible hardware/crane upgrades.
    Time Complexity: O(N * Capacity) [Pseudo-polynomial]
    """
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][capacity]
