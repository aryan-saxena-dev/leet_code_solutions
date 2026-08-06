class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def greet(n:int)->int:
            s=[]
            product=1
            while n>0:
                digit=n%10
                s.append(digit)
                n=n//10
            for i in s :
                product*=i
            return product
        while True:
            gay = greet(n)
            if gay%t==0:
                return n 
            else:
                n+=1
                               

        
         

        
       
                  
            

               

        