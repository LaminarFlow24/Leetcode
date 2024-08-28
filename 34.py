class Solution:
    def ubin(self, lis, l , r, num):
        m = (l+r) // 2
        if l == r:
            if lis[0] == num:
                return l
            if lis[0] != num:
                return -1

        if lis[m] > num:
            return self.ubin(lis, l, m, num)

        if lis[m] <= num:
            return self.ubin(lis, m ,r, num)

    def lbin(self, lis, l , r, num):
        m = (l+r) // 2
        if l == r:
            if lis[0] == num:
                return l
            if lis[0] != num:
                return -1
        if l 
        if lis[m] >= num:
            return self.lbin(lis, l, m, num)

        if lis[m] < num:
            print("l", l)
            print("r", r)
            return self.lbin(lis, m ,r, num)

        

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lis = []
        lis[0] = self.lbin(nums,0,len(nums)-1,target)
        # lis[1] = self.ubin(nums,0,len(nums)-1,target)
        return lis
