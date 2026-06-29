class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        Bucksort=[]
        answer=[]
        for i in range(len(nums)+1):
            Bucksort.append([])
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1
        for item in count :
            Bucksort[count[item]].append(item)
        for i in range(len(Bucksort) - 1, -1, -1):
            answer.extend(Bucksort[i])
            if len(answer) >= k:
                return answer[:k]
        return []



