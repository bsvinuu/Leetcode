class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n_list=[value for value in str(n)]
        n_set_list=list(set(n_list))

        score=0
        for value in n_set_list:
            freq=n_list.count(value)
            score+=int(value)*int(freq)
        return score