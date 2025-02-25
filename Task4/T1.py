# Nearest Prime
def near_prime(num):
    def is_prime(num):
        for i in range(2,int(((num)**0.5)+1)):
            if num % i == 0 :
                return False
        return True
    i = num-1
    j = num+1
    while True:
        if is_prime(i) and is_prime(j):
            return [i,j]
        elif is_prime(i):
            return [i]
        elif is_prime(j):
            return [j]
        else :
            i -= 1
            j += 1
        
num = int(input("Enter the number: "))
print("Nearest prime to the given number is, " , near_prime(num))