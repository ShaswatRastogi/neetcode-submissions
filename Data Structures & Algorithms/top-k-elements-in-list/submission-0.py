class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        answer=[]
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1

        sorted_item=sorted(count.items() , key=lambda item:item[1], reverse=True)
        for item in sorted_item[:k]:
            answer.append(item[0])
        return answer
