class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        kk = 0
        maxx = 0
        l = 0
        r = 0

        if nums[l] == 0:
            kk += 1

        while r < len(nums) - 1:
            if maxx < r - l:
                maxx = r - l
            if kk < k:
                if nums[r+1] == 0:
                    kk += 1
                    r += 1
                    continue
                if nums[r+1] == 1:
                    r += 1
                    continue

            if kk >= k:
                if nums[r+1] == 0:
                    if nums[l] == 0: 
                        l += 1
                        kk -= 1
                        continue
                    if nums[l] == 1:
                        l += 1
                        continue
                
                if nums[r+1] == 1:
                    r += 1
                    continue

        return maxx + 1
