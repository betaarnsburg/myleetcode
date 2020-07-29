#https://leetcode-cn.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            i = 0
            j = 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].islower():
                    i += 1
                else:
                    break
            if i == len(query) and j == len(pattern):
                res.append(True)
            else:
                res.append(False)
        return res
