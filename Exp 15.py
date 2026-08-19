def large_group_positions(s):

    result = []

    start = 0

    for i in range(1, len(s) + 1):

        if i == len(s) or s[i] != s[start]:

            if i - start >= 3:
                result.append([start, i - 1])

            start = i

    return result


# Test Case 1
s = "abbxxxxzzy"
print("Input:", s)
print("Output:", large_group_positions(s))

# Test Case 2
s = "abc"
print("\nInput:", s)
print("Output:", large_group_positions(s))