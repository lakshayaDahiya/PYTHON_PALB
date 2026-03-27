class Solution:
    def maxSubarraySum(self, arr):
        max_sum = arr[0]
        curr_sum = 0

        for x in arr:
            curr_sum += x
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0

        return max_sum
arr= list(map(int, input("Enter array elements: ").split()))
obj = Solution()
result = obj.maxSubarraySum(arr)
print(result)