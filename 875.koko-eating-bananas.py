#https://leetcode-cn.com/problems/koko-eating-bananas/description/

class Solution:
    def canEatAllBananas(self, piles, H, K):
        t = 0
        for pile in piles:
            t += math.ceil(pile / K)
        return t <= H
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            mid = (l + r) >> 1
            if self.canEatAllBananas(piles, H, mid):
                r = mid
            else:
                l = mid + 1
        return l
