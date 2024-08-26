class Solution:
    def fractionAddition(self, s: str) -> str:
        s = "+" + s
        
        print(s)
        nlis = []
        dlis = []

        for i in range(1,len(s)-2):
            if s[i+1] == '/':
                print("yay")
                if s[i-1] == '+':
                    nlis.append(int(s[i]))
                if s[i-1] == '-':
                    nlis.append(int(s[i])*(-1))

                dlis.append(int(s[i+2]))

        print(nlis)
        print(dlis)
        
        ndlis = dlis.sort()
        ndlis.reverse()
        
        m = 1

        for i in range(len(ndlis)):
            m *= ndlis[i]

            for j in range(i+1,len(ndlis)):
                if m % ndlis[j] != 0:
                    break
                if ndlis[j] == len(ndlis) - 1:
                    return m 

        for i in range(len(nlis)):
            nlis[i] = nlis[i] * (m / dlis[i])


        
        numm = sum(nlis)
        denm = m
    
        ss = ""

        ss += str(numm)
        ss += "/"
        ss += str(m)

        print(ss)
        
        
        
        
        return "hi"

        
            
