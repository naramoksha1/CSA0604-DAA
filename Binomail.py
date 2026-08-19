def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

n = int(input("Enter n: "))
k = int(input("Enter k: "))

print("Binomial Coefficient:", binomial(n, k))
