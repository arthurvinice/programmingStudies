# Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
# the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will 
# represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing 
# the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

def FindIntersection(strArr):
  arr1 = [int(x) for x in strArr[0].strip('[]"').split(', ')]
  arr2 = [int(x) for x in strArr[1].strip('[]"').split(', ')]
  arr3 = []
  for number in arr1:
    if number in arr2:
        arr3.append(number)
    
  if not arr3:
      return False
  return arr3

print(FindIntersection(input()))
