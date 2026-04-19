class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n

        # Next Smaller Element (right side)
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)

        # count total subarrays
        count = 0
        for i in range(n):
            count += (next_smaller[i] - i)

        return count


# Testing
if __name__ == "__main__":
    arr = [1, 2, 1]
    result = Solution().countSubarrays(arr)
    print("Count of valid subarrays:", result)
