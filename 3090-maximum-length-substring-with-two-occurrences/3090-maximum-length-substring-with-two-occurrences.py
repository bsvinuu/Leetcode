class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length=0
        left,right=0,1
        while left <=len(s) and right <=len(s):

            # print(s[left:right+1])
            occurence_dic={}
            for chara in s[left:right+1]:
                if chara not in occurence_dic:
                    occurence_dic[chara]=1
                else:
                    temp_count=occurence_dic.get(chara)
                    temp_count+=1
                    occurence_dic[chara]=temp_count
            # print(s[left:right+1])
            # print(occurence_dic)

            status=all([value if value <=2 else None for value in list(occurence_dic.values())])
            if status==True:
                max_length=max(max_length,len(s[left:right+1]))

            # print(s[left:right+1])
            # print(occurence_dic)
            # print(status)
            # print(len(s[left:right+1]))
            # print('-----')
            if right==len(s):
                left=left+1
                right=left+1


            # left+=1
            right+=1
        return max_length




        