class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        temp_nums=list(map(lambda x :x,str(num)))
        left,right=0,k-1
        output=0
        while left<len(temp_nums) and right<len(temp_nums) :
            number=int(''.join(temp_nums[left:right+1]))
            if number >=1:
                if num%number==0:
                    output+=1
            left+=1
            right+=1
        return output