class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # resMap = {i:nums.count(i) for i in nums}
        # resMap = dict(sorted(resMap.items(), key=lambda item: item[1], reverse=True))
        # cnt = 0
        # for key in resMap:
        #     if k == cnt:
        #         return res
        #     res.append(key)
        #     cnt += 1
        # return res
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for key,value in count.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


            


        