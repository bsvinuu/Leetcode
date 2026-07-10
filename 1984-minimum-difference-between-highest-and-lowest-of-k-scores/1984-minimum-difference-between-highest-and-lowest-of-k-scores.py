class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # if len(nums)==1:
        #     return 0
        # output=max(nums)-min(nums)
        # for  i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         # print(nums[i],nums[j])
        #         diff=abs(nums[i]-nums[j])
        #         output=min(output,diff)
        # return output


        nums.sort()
        output = float('inf')

        left = 0
        right = k - 1

        while right < len(nums):

            diff = nums[right] - nums[left]
            output = min(output, diff)

            left += 1
            right += 1

        return output
        