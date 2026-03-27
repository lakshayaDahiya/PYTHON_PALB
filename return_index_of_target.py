class Solution:
    def searchInsert(self,nums,target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
nums = list(map(int, input("Enter array for search:").split()))
target = int(input("Enter target to search in array:"))
obj = Solution()
result = obj.searchInsert(nums,target)
print(result)
                
