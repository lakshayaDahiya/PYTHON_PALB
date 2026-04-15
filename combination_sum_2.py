class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, path, target):
            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return result


# Testing
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    result = Solution().combinationSum2(candidates, target)
    print("Combinations:", result)
