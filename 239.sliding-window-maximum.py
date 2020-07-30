#https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, res, n = [], [], len(nums)
        for i in range(n):
            while deque and deque[0] < i - k + 1:
                deque.pop(0)
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop(-1)
            deque.append(i)
            if i >= k - 1: res.append(nums[deque[0]])
        return res
