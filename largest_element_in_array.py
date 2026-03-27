class Solution:
    def largest(self, arr):
        arr.sort()
        return arr[-1]
arr= list(map(int, input("Enter array elements: ").split()))
obj = Solution()
result=obj.largest(arr)
print(result)

#optimised 
# class Solution:
#     def largest(self, arr):
#         max_val = arr[0]
#         for x in arr:
#             if x > max_val:
#                 max_val = x
#         return max_val