class Solution:
    def missingNumber(self,arr,n):
        
        # for i in range(1,n+1):
        #     if i not in arr:
        #         return i
        
        # setArr = set()
        # for num in arr:
        #     setArr.add(num)
            
        # for i in range(1,n+1):
        #     if i not in setArr:
        #         return i
        
        
        sumN = n*(n+1)//2
        sumArr = 0
        for num in arr:
            sumArr += num
            
        return sumN - sumArr;
            
