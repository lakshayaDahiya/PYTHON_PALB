class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []

        for num in arr:
            while stack and stack[-1] >= num:
                stack.pop()

            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])

            stack.append(num)

        return result


# Testing
if __name__ == "__main__":
    arr = [1, 5, 0, 3, 4, 5]
    result = Solution().prevSmaller(arr)
    print("Previous Smaller Elements:", result)
