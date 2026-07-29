class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for i in range(len(words)+1)]

        for n in words:
            count[n] = 1 + count.get(n,0)
        for key, value in count.items():
            freq[value].append(key)
        res = []
        for i in range(len(words)-1,0,-1):
            for j in sorted(freq[i]):
                res.append(j)
                if len(res) == k:
                    return res
