class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        answer = []

        for i in range(len(nums)):
            suffix = 1

            if i == 0:
                prefix = 1
            else:
                prefix *= nums[i - 1]

            for j in range(i + 1, len(nums)):
                suffix *= nums[j]

            answer.append(prefix * suffix)

        return answer