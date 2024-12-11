class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for x in grid:
            if sum(x) == len(grid)-1:
                return grid.index(x)
