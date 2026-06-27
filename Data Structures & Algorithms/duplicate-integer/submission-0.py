class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return not len(nums) == len(num_set)
        