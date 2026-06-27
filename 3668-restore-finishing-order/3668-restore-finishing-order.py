class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [ord for ord in order if ord in friends]
        