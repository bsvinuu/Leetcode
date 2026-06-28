class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # temp_s=[letter for letter in s]
        # temp_t=[letter for letter in t]
        # return "".join(set(temp_t) - set(temp_s))
        temp_s=[letter for letter in s]
        temp_t=[letter for letter in t]

        for letter in temp_t:
            if letter in temp_s:
                temp_s.remove(letter)
            else:
                return letter