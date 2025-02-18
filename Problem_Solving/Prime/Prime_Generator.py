# NOTE : Method 1 : using generator
def prime_generator(n):
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num  # Yield the prime number

n = int(input("Enter the range: "))

print("Prime numbers:", list(prime_generator(n)))

# NOTE : Method 2 : using list comprehension
# def primes(n):
#     primes = [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
#     return primes

# print("Prime numbers:", primes(n))

# NOTE : Method 3 : using for loop
# def primes(n):
#     primes = []
#     for i in range(2, n + 1):
#         is_prime = True
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(i)
#     return primes

# print("Prime numbers:", primes(n))