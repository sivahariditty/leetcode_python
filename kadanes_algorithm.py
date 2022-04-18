#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        maxval = arr[0]
        max_til_here = arr[0]
        for i in range(1, N):
            if(max_til_here + arr[i] < arr[i]):
                max_til_here = arr[i]
            else:
                max_til_here = max_til_here + arr[i]
            if(maxval < max_til_here):
                maxval = max_til_here
        return maxval

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
