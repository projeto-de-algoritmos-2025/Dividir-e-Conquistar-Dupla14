from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for x in nums[1:]:
            # Escolhe entre começar um novo subarray ou continuar o atual
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far