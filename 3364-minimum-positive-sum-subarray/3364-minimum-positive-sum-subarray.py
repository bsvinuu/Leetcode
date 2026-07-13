class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_subarray_sum=float('inf')
        for window_size in range(l,r+1):
            left,right=0,window_size
            while left < len(nums) and right <=len(nums) :
                # print(nums[left:right],sum(nums[left:right]))
                # print(left,right)
                if sum(nums[left:right])>0 and  sum(nums[left:right]) < min_subarray_sum:
                    min_subarray_sum=min(min_subarray_sum,sum(nums[left:right]))
                    # output.append(list(nums[left:right]))
                right+=1
                left=left+1
        if min_subarray_sum == float('inf'):
            return -1
        else:
            return min_subarray_sum
        