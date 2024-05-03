def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    if 1 <= len(hours) <= 50:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count
