class Solution:
    def convert(self, s):
        lis = []
        for i in range(len(s)):
            lis.append(s[i])

        if len(lis) % 2 != 0:
            m = len(lis) // 2
            for i in range(1,(len(s)//2)+1):
                lis[m+i] = lis[m-i] 

        if len(lis) % 2 == 0:
            m = len(lis) // 2
            n = (len(lis) // 2) - 1

            for i in range(0,(len(s)//2)):
                lis[m+i] = lis[n-i]

        m = ""

        for i in range(len(s)):
            m += lis[i] 

        return m

    def nearestPalindromic(self, n: str) -> str:
        temp = int(self.convert(n))
        num = int(n)
        onum = int(n)
        

        

        if temp > num:
            num -= (temp-num)
            ans = self.convert(str(num))
            ans = int(ans)
            
            while(ans > num and ans < onum):
                ans = self.convert(str(num))
                ans = int(ans)
            
            return ans 
            # if ans > num:
            #     return ans
            # else:
            #     return temp

        if temp < num:
            num += (num-temp)
            ans = self.convert(str(num))
            ans = int(ans)
            if ans < num:
                return ans
            else:
                return temp 
        
        

        
        
    
