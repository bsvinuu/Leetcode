class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # outp  ut=[]
        # for num in nums1:
        #         index=nums2.index(num) 
        #         if len(nums2)>index+1 and nums2[index+1]>num:
        #             output.append(nums2[index+1])
        #         else:
        #             output.append(-1)
        # return output
        output=[]
        for num in nums1:
                index=nums2.index(num)
                if len(nums2)>index+1 and any(map(lambda x:x if x>num else None,nums2[index+1::])):

                    output.append(next(i for i in nums2[index+1::] if i>num ))
                else:
                    output.append(-1)
        return output