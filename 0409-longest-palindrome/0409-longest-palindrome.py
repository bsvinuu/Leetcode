class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_temp={}
        for value in s:
            if value not in freq_temp:
                freq_temp[value]=1
            else:
                temp_value=freq_temp.get(value)+1
                freq_temp[value]=temp_value
        even=0
        odd=set()
        for key,value in freq_temp.items():
            if value%2==0:
                even+=value
            elif value%2 !=0:
                # odd.add(value)
                if value >1:
                    even+=value-1
                    odd.add(1)
                elif value ==1:
                    odd.add(1)
        return sum(odd)+even
        