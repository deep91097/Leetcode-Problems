class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {} #Hashmap for storing the actual value in the array nums and their count
        # res, maxCount = 0,0 # variables to keep track of res and MaxCount of that value
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n],maxCount)
        # return res

        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += 1 if res == n else -1
        return res

        