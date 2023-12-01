# function sumNums - use recursion to find the sum of all numbers from 1 to the given 'num'

def sumNums(num):
    total_sum = 0

    for i in range(1, num + 1):
        total_sum += i

    return total_sum

result = sumNums(3)
print(result)