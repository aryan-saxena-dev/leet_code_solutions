class Solution:
    def maxProduct(self, n: int) -> int:
        p = n
        nums =[]
        max=0
        s_max=float('-inf')
        while p >0 :
            digit = p%10
            nums.append(digit) 
            p=p//10
        for num in nums :
            if num > max:
                s_max =max
                max =num
            elif max >=num  and num> s_max:
                s_max = num
        return max*s_max     


        return max*s_max
sol = Solution()
assert sol.maxProduct(234)== 12
print("passed")
    


        
        