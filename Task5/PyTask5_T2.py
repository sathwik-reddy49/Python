# Sum of first n non fib numbers
def non_fib_sum(n):
    non_fib = set()
    cur_num = 1

    def isFib(n1):
        a,b = 0,1
        fib = set()
        while a <= n1 :
            fib.add(a)
            a,b = b,a+b
        return n1 in fib
    
    while len(non_fib) < n :
        if isFib(cur_num) == False :
            non_fib.add(cur_num)
        cur_num += 1
    return sum(non_fib)

num = int(input("Enter a number to find the sum of first n non fib numbers : "))
print(non_fib_sum(num))