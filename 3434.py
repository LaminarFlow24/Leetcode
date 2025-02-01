class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        coords = []
        nums.append(1000000)

        for i in range(len(nums)):
            if nums[i] == k:
                coords.append(i)

        if len(coords) == 1:
            print("hi")
            p = coords[0]
            return(max(self.countm(nums[0:p]), self.countm(nums[p+1:]))) + 1

        maxx = 0
        for i in range(len(coords) - 1):
            if maxx < self.countm(nums[coords[i] + 1 : coords[i+1]]):
                maxx = self.countm(nums[coords[i] + 1 : coords[i+1]])

        return maxx + len(coords)


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

        return v
