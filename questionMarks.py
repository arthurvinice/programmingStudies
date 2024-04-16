# Questions Marks
# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

def QuestionsMarks(strParam):
  qmarks = 0
  n2 = 0
  sum_10 = False
  match = False
  for char in strParam:
      if char.isdigit():
        n1 = int(char)
        if n1 + n2 == 10:
            sum_10 = True
            if qmarks != 3:
                return False
            else:
                match = True
                return match
        qmarks = 0
        n2 = n1
      elif char == '?':
          qmarks += 1

  # code goes here
  return match

# keep this function call here 
print(QuestionsMarks(input()))
