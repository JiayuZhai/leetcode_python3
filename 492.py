import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(1,int(math.sqrt(area))+1)[::-1]:
            if area % i == 0:
                return [area//i,i]
        return None
