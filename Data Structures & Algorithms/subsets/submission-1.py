class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, path):
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            
            res.append(path[:])
        
        backtrack(0, [])
        return res