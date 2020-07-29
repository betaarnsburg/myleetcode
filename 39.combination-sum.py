#https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        size = len(candidates)
        if size <= 0:
            return []    
        candidates.sort()       
        path = []
        res = []
        self._find_path(target, path, res, candidates, 0, size)
        
        return res
        
    def _find_path(self, target, path, res, candidates, begin, size):

        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]

                if left_num < 0:
                    break
                path.append(candidates[i])
                self._find_path(left_num, path, res, candidates, i, size)
                path.pop()
