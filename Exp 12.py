def rob_linear(houses):
    prev1 = 0
    prev2 = 0

    for money in houses:
        temp = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = temp

    return prev1


def rob(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Test Case 1
nums = [2, 3, 2]
print("Input:", nums)
print("Maximum Money:", rob(nums))

# Test Case 2
nums = [1, 2, 3, 1]
print("\nInput:", nums)
print("Maximum Money:", rob(nums))