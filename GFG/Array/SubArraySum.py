class Solution:
    def subArraySum(self,arr, n, s): 
        
        #brute force
        
        # for i in range(n):
        #   rSum = 0
        #   for j in range(i,n):
        #         rSum += arr[j]
        #         if rSum == s:
        #             return [i+1, j+1]
        # return [-1]
        
        #optimized, prefix sum + sliding window
        if s == 0:
            return [-1]
        prefixSum = [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1]+arr[i])
        # print(prefixSum)
            
        l, r = 0, 0
        rSum = 0
        
        while r<n:
            
            rSum = prefixSum[r+1] - prefixSum[l]
            # print (rSum, l, r+1)
            if rSum == s:
                return [l+1,r+1]
            elif rSum < s:
                r += 1
            else:
                l += 1
        return [-1]
