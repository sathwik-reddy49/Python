# NOTE : Method 1: Using for loop
# num = int(input("Enter the number: "))
# feb = [0,1]
# for i in range(2,num):
#     feb.append(feb[i-1]+feb[i-2])
# print("".join(str(i) for i in feb))


# NOTE : Method 2: Using recursion
# def fibonacci(n):
#     feb = [0, 1]
#     while len(feb) < n:
#         feb.append(feb[-1] + feb[-2])
#     return feb

# num = int(input("Enter the number: "))
# print("".join(str(i) for i in fibonacci(num)))


# NOTE : Method 3: Using generator
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield (a)
        a, b = b, a + b

num = int(input("Enter the number: "))
print("".join(str(i) for i in fibonacci_generator(num)))