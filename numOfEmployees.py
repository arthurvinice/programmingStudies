# There are n employees in a company, numbered from 0 to n - 1.
# Each employee i has worked for hours[i] hours in the company.
# The company requires each employee to work for at least target hours.
# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
# Return the integer denoting the number of employees who worked at least target hours.

# Challenge available in leetcode.com

def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    if 1 <= len(hours) <= 50:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count
