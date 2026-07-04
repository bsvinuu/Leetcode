class Solution:
    def romanToInt(self, s: str) -> int:
        " can do it another method as well like iterating the values from reverse order that is much more effiecnt"
        mapping_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
        total_len=len(list(map(lambda x:x,s)))
        output=0
        for index,symbol in enumerate(s):
            if total_len-1 !=index:
                # print(index)
                if symbol=='I' and s[index+1] in ('V','X'):
                    output-=mapping_dict[symbol]
                elif symbol=='X' and s[index+1] in ('L','C'):
                    output-=mapping_dict[symbol]
                elif symbol=='C' and s[index+1] in ('D','M'):
                    output-=mapping_dict[symbol]
                else:
                    output+=mapping_dict[symbol]
            else:
                output+=mapping_dict[symbol]              
        return output