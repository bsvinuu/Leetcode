class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        'solution one liner but time complexicity is high because of count'
        # temp_list=list(map(lambda x : x if nums.count(x)==1 else 0,nums))
        # return sum(temp_list)
        'this is get the freq count and filter the elements and extract the values'
        freq_dic={}
        for value in nums:
            if value not in freq_dic:
                        freq_dic[value]=1
            else:
                temp_value=freq_dic.get(value)
                temp_value+=1
                freq_dic[value]=temp_value
        final_output=[]
        for key,value in freq_dic.items():
            if value==1:
                    final_output.append(key)

        return sum(final_output)  





        