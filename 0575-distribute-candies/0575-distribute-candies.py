class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        no_of_unique_candy,max_candy_eat=len(list(set(candyType))),len(candyType)//2
        if max_candy_eat<=no_of_unique_candy:
            return max_candy_eat
        else:
            return no_of_unique_candy
            