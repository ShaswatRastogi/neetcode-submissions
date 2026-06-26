class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            sorts = "".join(sorted(str))
            if sorts not in groups:
                groups[sorts] = []
            groups[sorts].append(str)
        return list(groups.values())
