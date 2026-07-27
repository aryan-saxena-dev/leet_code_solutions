class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        s_max=float('-inf')
        for num in nums :
            if num >max :
                s_max=max
                max=num
            elif max >= num and num >s_max:
                s_max =num     

        
        return (max-1)*(s_max-1)
        