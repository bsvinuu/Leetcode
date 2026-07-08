class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        temp_list=list(map(lambda x :x ,s))
        if len(temp_list)<=1:
            return ''
        left,right=0,1
        output=[]
        while left<len(temp_list) :
            # print(temp_list[left:right+1])
            # checking_lower= list(set(filter(str.islower,temp_list[left:right+1])))
            # checking_upper= list(set(filter(str.isupper,temp_list[left:right+1])))
            # testing=list(map(lambda x : x.lower(),checking_upper))
            checking_lower= set(filter(str.islower,temp_list[left:right+1]))
            checking_upper= set(filter(str.isupper,temp_list[left:right+1]))
            testing=set(map(lambda x : x.lower(),checking_upper))

            # print(checking_lower)
            # print(checking_upper)
            # print('-----')
            # # break
            if checking_lower == testing:
                # print(temp_list[left:right+1])
                value=''.join(temp_list[left:right+1])
                output.append(value)
                # print(value)
            
            right+=1
            if right==len(temp_list):
                left+=1
                right=left+1
            if left== len(temp_list)-1:
                break
                # pass
            # print(left,right)
        output.sort(key=len,reverse=True)
        if len(output)>=1:
            return output[0]
        else:
            return ''