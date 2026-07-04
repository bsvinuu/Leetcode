class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        temp_list=list(map(lambda x : x if nums.count(x)==1 else 0,nums))
        return sum(temp_list)


        