class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def func(nums, idx: int, curr: List[int]):
            if len(nums) == idx:
                res.append(curr[:])
                return
            else:
                func(nums, idx+1, curr)
                func(nums, idx+1, curr + [nums[idx]])
                return
        
        func(nums, 0, [])
        return res