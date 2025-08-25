# 1.Evennumbers:

class Evennumbers():
    
    def __init__(self,limit):
        self.limit=limit
        self.num=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num+=2
        if self.num>self.limit:
            raise StopIteration
        return self.num

for num in Evennumbers(20):
    print(num)      


# 2. Generator for Squares  
    
def squares_upto_n(n) :
    count=1
    while count<=n:
        yield count**2
        count +=1
        
for nums in squares_upto_n(10):
    print(nums)
    
 