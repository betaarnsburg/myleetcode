#https://leetcode-cn.com/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.fraq = collections.defaultdict(lambda: 0)
        self.fraq_stack = collections.defaultdict(list)
        self.max_fraq = 0
        
    def push(self, x: int) -> None:
        self.fraq[x] += 1
        if self.fraq[x] > self.max_fraq:
            self.max_fraq = self.fraq[x]
        self.fraq_stack[self.fraq[x]].append(x)    
        
    def pop(self) -> int:
        ans = self.fraq_stack[self.max_fraq].pop()
        self.fraq[ans] -= 1
        if not self.fraq_stack[self.max_fraq]:
            self.max_fraq -= 1
        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
