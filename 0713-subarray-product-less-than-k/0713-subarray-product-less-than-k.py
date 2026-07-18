# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         ''' without using the sliding window it will work but the time complexicity because 
#         each time we are slicing so it wont work'''
#         # subarray=[]
#         # for k_value in range(1,len(nums)+1):
#         #     left,right=0,k_value
#         #     while left < len(nums) and right <= len(nums):
#         #         if math.prod(nums[left:right])<k:
#         #             subarray.append(nums[left:right])
#         #         right+=1
#         #         left+=1
#         # return len(subarray)
#         ''' this will handle the time complexicity  for sure because we are using sliding winow approach but still we can reduce the time complxicity by reducing the iteration'''
#         # subarray=[]
#         counter=0
#         for k_value in range(1,len(nums)+1):
#           left,right=0,k_value
#           product= math.prod(nums[left:right])
#           if product < k:
#             #   subarray.append(nums[left:right])
#             counter+=1
#           while left < len(nums) and right < len(nums):
#                step1=product//nums[left] 
#                step2=step1*nums[right]
#                if step2 <k:
#                     # subarray.append(nums[left:right])
#                     counter+=1
#                right+=1
#                left+=1
#                product=step2
#         return len(subarray)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):

            # Expand the window
            product *= nums[right]

            # Shrink until product becomes valid
            while product >= k:
                product //= nums[left]
                left += 1

            # Count all valid subarrays ending at 'right'
            count += (right - left + 1)

        return count

