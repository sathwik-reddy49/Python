



# Task 2
def sum_of_max_min_primes(num):
    num_str = str(num)
    maxi = int(num_str[0])
    mini = int(num_str[0])
    for i in num_str :
        if int(i) > 1 :
            for j in range(2, int(int(i) ** 0.5 + 1)):
                if (int(i) % j) == 0:
                    break
            else:
                if int(i) > maxi:
                    maxi = int(i)
                if int(i) < mini:
                    mini = int(i)
    return maxi + mini

num = int(input("Enter the number: "))
print("Sum of highest and lowest prime numbers in",num,":",sum_of_max_min_primes(num))