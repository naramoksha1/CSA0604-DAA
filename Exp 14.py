def unique_paths(m, n):

    dp = [[1 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


# Test Case 1
m = 7
n = 3
print("Input: m =", m, "n =", n)
print("Output:", unique_paths(m, n))

# Test Case 2
m = 3
n = 2
print("\nInput: m =", m, "n =", n)
print("Output:", unique_paths(m, n))