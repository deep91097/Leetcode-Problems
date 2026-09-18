class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        MapST, MapTS = {}, {}
        for c1, c2 in zip(s, t):
            if ((c1 in MapST and MapST[c1] != c2) or
            (c2 in MapTS and MapTS[c2] != c1)):
                return False

            MapST[c1] = c2
            MapTS[c2] = c1
        return True
        