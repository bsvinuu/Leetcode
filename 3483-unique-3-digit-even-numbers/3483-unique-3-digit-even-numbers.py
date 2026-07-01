class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # result = ["".join(map(str, p)) for p in itertools.permutations(digits, 3)]
        # # list(map(lambda x :int(x) if int(x)%2==0 else None,result))
        # filter_numbers=list(filter(lambda x: int(x)%2==0 ,result))
        # return len(list(map(lambda x: int(x),filter_numbers)))
        import itertools
        result = list(set(["".join(map(str, p)) for p in itertools.permutations(digits, 3)]))
        filter_numbers=list(filter(lambda x :x[0] != '0' and int(x) % 2 == 0,result))
        return len(filter_numbers)
        