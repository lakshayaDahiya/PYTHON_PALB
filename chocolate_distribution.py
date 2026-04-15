class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)

        if m > n:
            return -1

        arr.sort()

        min_diff = float('inf')

        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff


# Testing
if __name__ == "__main__":
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    result = Solution().findMinDiff(arr, m)
    print("Minimum difference:", result)
