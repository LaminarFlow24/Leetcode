class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        lis = []
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i+1] % 2:
                lis.append(i)

        booll = []
        q = sorted(queries, key=lambda x: (x[0], x[1]))
        
        a = 0
        b = 0

        print(lis)
        while( b < len(q)):
            print("hi")
            if a == len(lis):
                print("ham")
                while(b < len(q)):
                    booll.append(True)
                    b += 1
                break

            if q[b][0] <= lis[a] < q[b][1]:
                print("seb")
                booll.append(False)
                a += 1
                b += 1
                continue
            
            if q[b][1] <= lis[a]:
                print("max")
                booll.append(True)
                b += 1
                continue

            if lis[a] < q[b][0]:
                print("alo")
                a += 1
                continue

            return booll
