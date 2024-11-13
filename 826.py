class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        lis = []
        l = 0
        maxx = 0
        prof = 0
        worker.sort()
        for i in range(len(difficulty)):
            lis.append([difficulty[i], profit[i]])

        slis = sorted(lis, key=lambda x: x[0])

        for i in range(len(worker)):
            print(i)
            while True:
                if worker[i] >= slis[l][0]:
                    l += 1
                    temp = slis[l][1]

                    if temp > maxx:
                        maxx = temp
                    
                if worker[i] < slis[l][0]:
                    if l != 0:
                        l -= 1
                    break
                print(maxx,i,l)

            prof += maxx
            print(prof,i)

        return prof
