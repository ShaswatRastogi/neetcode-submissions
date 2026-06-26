class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
           invert = target - nums[i]
           if (invert in seen) :
                return [seen[invert],i]
           if nums[i] not in seen:
                seen[nums[i]]=i

        return []
              
        

