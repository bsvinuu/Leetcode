class Solution:
    def maxLength(self, nums: List[int]) -> int:
        left,right=0,1
        max_length=0
        try:
            while left <len(nums) and right <= len(nums):
                subarray=nums[left:right+1]
                if math.prod(subarray)== math.lcm(*subarray)* math.gcd(*subarray):
                    max_length=max(max_length,len(subarray))
                    print(subarray,len(subarray))
                if right == len(nums):
                    left=left+1
                    right=left+1
                right+=1
            return max_length
        except Exception as e :
            return e