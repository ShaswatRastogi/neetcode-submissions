class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""

        for str1 in strs:
            a = len(str1)
            b = str(a) + "#" + str1
            s += b

        return s

    def decode(self, s: str) -> List[str]:
        jump = 0
        seen = ""
        answer = []
        while jump < len(s):
            if s[jump] == "#":
                answer.append(s[jump + 1 : jump + 1 + int(seen)])
                jump = jump + 1 + int(seen)
                seen = ""
            else:
                seen = seen + s[jump]
                jump += 1
        return answer
