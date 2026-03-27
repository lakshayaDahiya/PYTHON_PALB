class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
nums = list(map(int, input("Enter array for search:").split()))
target = int(input("Enter target to search in array:"))
obj = Solution()
result = obj.twoSum(nums,target)
print(result)