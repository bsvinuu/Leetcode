class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_value=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if abs(nums[i]-nums[j])<= min(nums[i],nums[j]):
                    if (nums[i]^nums[j])>max_value:
                            max_value=nums[i]^nums[j]

        return max_value