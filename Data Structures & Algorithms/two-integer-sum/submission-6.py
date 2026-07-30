class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        
        hash_map = {}
        for j in range(len(nums)):
            num = target - nums[j]
            if num in hash_map:
                return [hash_map[num], j]
            hash_map[nums[j]] = j
