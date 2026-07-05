import numpy as np
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # left,right=0,k-1
        # max_mean=0
        # if len(nums)<=k:
        #     return np.mean(nums)
        # while left<=(len(nums)-k):
        #     # print(left,right,np.mean(nums[left:right+1]),nums[left:right+1])
        #     if max_mean<np.mean(nums[left:right+1]):
        #         max_mean=np.mean(nums[left:right+1])
        #     left+=1
        #     right+=1
        # return max_mean


        left,right=0,k
        max_mean=0
        sum_value=sum(nums[left:right])
        length_value=len(nums[left:right])
        if len(nums)<=k:
            return np.mean(nums)
        max_mean=sum_value/length_value
        while left<=(len(nums)-k) and len(nums)!=right :
            temp_sum=sum_value-nums[left]
            temp_sum+=nums[right]
            temp_mean=temp_sum/length_value
            sum_value = temp_sum
            if temp_mean>max_mean:
                max_mean=temp_mean
            left+=1
            right+=1
            max_mean = max(max_mean, temp_mean)
        return max_mean