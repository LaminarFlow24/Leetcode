class Solution:
    def hc(self, n):
        for i in range(n-1,1,-1):
            if n % i == 0:
                return i
            if i == 2:
                return n
        return n
    
    def rec(self, n,ans):
        if n == 1:
            return ans
        ans += ((n/self.hc(n)) - 1)
        print(ans,"ans")
        n /= self.hc(n)
        n = int(n)
        return self.rec(n,ans)

    def minSteps(self, n: int) -> int:
        anss = 0
        return self.rec(n,anss)
