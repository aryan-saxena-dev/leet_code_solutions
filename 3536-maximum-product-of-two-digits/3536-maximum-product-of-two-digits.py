class Solution:
    def maxProduct(self, n: int) -> int:
        p = n
        nums =[]
        max=0
        s_max=float('-inf')


        while p> 0:
            digit = p%10
            nums.append(digit)
            p=p//10
        for  i in range(len(nums)):
            if nums[i] > max:
                s_max=max
                max =nums[i]
            

            elif  max >= nums[i] and nums[i] > s_max :
                s_max= nums[i]

        return max*s_max




        
        