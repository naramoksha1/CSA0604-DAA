def climb_stairs(n):

    if n == 1:
        return 1

    if n == 2:
        return 2

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


# Test Case 1
n = 4
print("Input:", n)
print("Ways:", climb_stairs(n))

# Test Case 2
n = 3
print("\nInput:", n)
print("Ways:", climb_stairs(n))