class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} # Hashmap  for counting storing the nums
        res, MaxCount = 0,0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if MaxCount < count[n] else res
            MaxCount = max(count[n],MaxCount)

        return res
        