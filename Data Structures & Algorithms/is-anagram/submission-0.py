class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count = {}
        for char in s:
            if char not in count:
                count[char]=0
            count[char]+=1

        count1={}
        for char1 in t:
            if char1 not in count1:
                count1[char1]=0
            count1[char1]+=1
        
        if count==count1:
            return True
        return False