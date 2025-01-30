# inp = input("Enter the number: ")
# result = ""
# for i in inp:
#     if i == "0":
#         result+= "1"
#     elif i == "1":
#         result+= "0"
#     else:
#         result+= i
# print(int(result))

inp = input("Enter the number: ")
inp_sum = 0
for i in inp:
    inp_sum = inp_sum + int(i)
if(int(inp)%inp_sum == 0):
    print("It is a harshard number")
else:
    print("It is not a harshard number")