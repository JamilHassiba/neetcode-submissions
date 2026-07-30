class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        
        prev_map = {}
        for j, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], j]
            prev_map[n] = j
