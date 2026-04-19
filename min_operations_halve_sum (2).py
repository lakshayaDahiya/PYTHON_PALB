import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2

        # max heap (use negative values)
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        current_sum = total
        operations = 0

        while current_sum > target:
            largest = -heapq.heappop(max_heap)
            half = largest / 2

            current_sum -= half
            heapq.heappush(max_heap, -half)

            operations += 1

        return operations


# Testing
if __name__ == "__main__":
    arr = [8, 6, 2]
    result = Solution().minOperations(arr)
    print("Minimum operations:", result)
