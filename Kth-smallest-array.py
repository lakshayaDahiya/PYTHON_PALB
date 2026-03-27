class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]
# Take input
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

# Create solution object
solobj = Solution()
result = solobj.kthSmallest(arr, k)
print(f"The {k}th smallest element is: {result}")