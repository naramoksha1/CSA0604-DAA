from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
min_cost = float('inf')
best_path = None

for path in permutations(range(1, n)):
    current_path = (0,) + path
    total = 0

    for i in range(n - 1):
        total += cost[current_path[i]][current_path[i + 1]]

    total += cost[current_path[-1]][0]

    if total < min_cost:
        min_cost = total
        best_path = current_path

print("Minimum Cost:", min_cost)
print("Best Path:", [x + 1 for x in best_path] + [1])
