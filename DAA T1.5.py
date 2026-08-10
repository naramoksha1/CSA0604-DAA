nums = list(map(int, input().split()))

maximum = nums[0]

for i in nums:
    if i > maximum:
        maximum = i

print(maximum)
