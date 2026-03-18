class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNums = {}
        for i,num in enumerate(nums):
            other = target - num
            if other in mapNums:
                return [i, mapNums[other]]
            
            mapNums[num] = i

            