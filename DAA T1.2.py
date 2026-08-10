nums1 = [2, 3, 2]
nums2 = [1, 2]

answer1 = 0
answer2 = 0

for i in nums1:
    if i in nums2:
        answer1 += 1

for i in nums2:
    if i in nums1:
        answer2 += 1

print([answer1, answer2])
