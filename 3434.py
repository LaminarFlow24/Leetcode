class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        coords = []
        nums.append(1000000)
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] == k:
                coords.append(i)

        
        nk = len(coords)
        coords = [-1] + coords
        coords = coords + [len(nums) - 1]
        print(coords)



        maxx = 0
        for i in range(len(coords) - 1):
            if maxx < self.countm(nums[coords[i] + 1 : coords[i+1]]):
                maxx = self.countm(nums[coords[i] + 1 : coords[i+1]])

        print(maxx,nk)
        return maxx + nk


    def countm(self, lis):
        dicc = {}
        flag = False
        for i in range(len(lis)):
            try:
                dicc[lis[i]] += 1
            except:
                dicc[lis[i]] = 1

        sorted_by_values = dict(sorted(dicc.items(), key=lambda item: item[1]))


        for key,value in sorted_by_values.items():
            v = value
            k = key
            flag = True

        if flag == False:
            return 0
        print(key,"key")
        return v
