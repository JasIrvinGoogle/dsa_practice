# Linear runtime solution
# Iterate through each number in list = o(n)
# Initialize/start at 0, go through each number in the list, update result -> for loop

nums1 = [2,2,1]
result1 = 0
for num in nums1:
    result1 ^= num #bitwise operation XOR - 'a = a^b'
print(f"Example 1: {result1}")

nums2 = [4,1,2,1,2]
result2 = 0
for num in nums2:
    result2^= num
print(f"Example 2: {result2}")

nums3 = [1]
result3 = 0
for num in nums3:
    result3^= num
print(f"Example 3: {result3}")