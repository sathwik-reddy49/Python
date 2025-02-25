# Flip Bits
inp = input("Enter the number: ")
result = ""
for i in inp:
    if i == "0":
        result+= "1"
    elif i == "1":
        result+= "0"
    else:
        result+= i
print(int(result))