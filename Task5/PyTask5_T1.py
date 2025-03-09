# Method 1 : Inbuilt Function
# def decimal_to_binary(num):
#     return bin(num)[2:]
# num = int(input("Enter a Number to convert into Binary Number : "))
# print("Binary:", decimal_to_binary(num))

# Method 2 : Normal Process
def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary if binary else "0"

num = int(input("Enter a Number to convert into Binary Number : "))
print("Binary:", decimal_to_binary(num))