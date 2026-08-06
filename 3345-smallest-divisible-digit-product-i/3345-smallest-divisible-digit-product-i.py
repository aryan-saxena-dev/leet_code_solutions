class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product=1

            for i in str(n):
                product*=int(i)
            if product%t==0:

                return n
            else:
                n+=1 
                       

        
       
                  
            

               

        