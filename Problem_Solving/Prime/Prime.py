num = int(input("Enter the number: "))
num_str = str(num)
primes = []
for i in num_str :
    if int(i) > 1 :
        for j in range(2, int(int(i) ** 0.5 + 1)):
            if (int(i) % j) == 0:
                break
        else:
            primes.append(int(i))
print("Given number is",num)
print("Prime numbers in",num,"".join(str(i) for i in primes))

# Find the sum of all prime numbers in the given number
prime_sum = sum(primes)
print("Sum of prime numbers in",num,":",prime_sum)

# Find the product of all prime numbers in the given number
prime_product = 1
for i in primes:
    prime_product *= i
print("Product of prime numbers in",num,":",prime_product)

# Find the largest prime number in the given number
print("Largest prime number in",num,":",max(primes))

# Find the smallest prime number in the given number
print("Smallest prime number in",num,":",min(primes))

# Find the average of all prime numbers in the given number
print("Average of prime numbers in",num,":",prime_sum/len(primes))

# Find the median of all prime numbers in the given number
print("Median of prime numbers in",num,":",sum(primes)/len(primes))

# Find the mode of all prime numbers in the given number
print("Mode of prime numbers in",num,":",max(set(primes), key = primes.count))