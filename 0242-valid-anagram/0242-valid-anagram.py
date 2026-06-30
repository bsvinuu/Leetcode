class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_temp=[letter for letter in s]
        t_temp=[letter for letter in t]

        s_dic={}
        for letter_s in s_temp:
            if letter_s in s_dic:
                value=s_dic.get(letter_s)+1
                s_dic[letter_s]=value
            else:
                s_dic[letter_s]=1

        t_dic={}
        for letter_s in t_temp:
            if letter_s in t_dic:
                value=t_dic.get(letter_s)+1
                t_dic[letter_s]=value
            else:
                t_dic[letter_s]=1

        # for key,values in s_dic.items():
        #     # print(key,values)
        #     if t_dic.get(key) is None:
        #         return False
        #     if values>=t_dic.get(key):
        #         continue
        #     else:
        #        return False
        # if len(s) != len(t):
        #     return False

        if s_dic==t_dic:
            return True
        else:
            return False
        # return True
