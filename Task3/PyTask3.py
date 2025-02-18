def nearest_fibonacci(n):
    if n == 0:
        return 0
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    # Find the closest Fibonacci number
    if abs(a - n) <= abs(b - n):
        return a
    else:
        return b

# Input from user
num = int(input("Enter number: "))
print("Nearest Fibonacci number:", nearest_fibonacci(num))