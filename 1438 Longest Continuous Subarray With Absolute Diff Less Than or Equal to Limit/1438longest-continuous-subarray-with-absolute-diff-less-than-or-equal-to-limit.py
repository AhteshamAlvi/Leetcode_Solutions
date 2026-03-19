from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        minq = deque()
        maxq = deque()
        result = 0

        for j in range(len(nums)):
            
            while maxq and maxq[-1] < nums[j]:
                maxq.pop()
            maxq.append(nums[j])

            while minq and minq[-1] > nums[j]:
                minq.pop()
            minq.append(nums[j])

            while maxq[0] - minq[0] > limit:
                
                if nums[i] == maxq[0]:
                    maxq.popleft()
                if nums[i] == minq[0]:
                    minq.popleft()
                i += 1

            result = max(result, j - i + 1)

        return result
