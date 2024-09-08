def findTwoDistinct(arr):
    xor = 0
    num1 = 0
    num2 = 0

 
    for num in arr:
        xor ^= num

    set_bit = xor & ~(xor - 1)

    
    for num in arr:
        if num & set_bit:
            num1 ^= num  
        else:
            num2 ^= num  
    return sorted([num1, num2])

N = int(input("Enter the value of N: "))
arr = list(map(int, input(f"Enter {2 * N + 2} elements: ").split()))


result = findTwoDistinct(arr)
print(result[0], result[1])