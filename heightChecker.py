def heightChecker(heights: list[int]) -> int:
    if  1 <= len(heights) <= 100:
        h_sorted = sorted(heights)
        dif = 0
        for i in range(len(h_sorted)):
            if heights[i] != h_sorted[i]:
                dif += 1
        return dif
