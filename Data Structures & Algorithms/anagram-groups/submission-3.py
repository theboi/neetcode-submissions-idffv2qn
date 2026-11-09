from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pools = defaultdict(list)
        for s in strs:
            counter = defaultdict(int)
            for ch in s:
                counter[ch] += 1
            pools[hash(frozenset(counter.items()))].append(s)
        return list(pools.values())