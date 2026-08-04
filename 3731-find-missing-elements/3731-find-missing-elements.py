class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        seen= set(nums)
        r=1
        s=[]
        for i in range(min(nums),max(nums)):
            if i not in seen:
                s.append(i)

        return s     


            
        
        