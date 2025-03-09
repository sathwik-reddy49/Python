# Method 1 : Right rotate using reversing Array
# def rotate(nums,k):
#     n = len(nums)
#     k = k%n
#     def reverse(nums,start,end):
#         while start < end :
#             nums[start],nums[end] = nums[end],nums[start]
#             start += 1
#             end -= 1
#     reverse(nums,0,n-k-1)
#     reverse(nums,n-k,n-1)
#     reverse(nums,0,n-1)
#     return nums

# nums = list(map(int,input("Enter array numbers with spaces : ").split()))
# k = int(input("Enter no of elements to rotate : "))
# print(rotate(nums,k))

# Method 2 : Right rotate using slicing
def rotate(nums,k):
    k=k%len(nums)
    nums[:]= nums[-k:]+nums[:-k]
    return nums[:]

nums = list(map(int,input("Enter array numbers with spaces : ").split()))
k = int(input("Enter no of elements to rotate : "))
print(rotate(nums,k))