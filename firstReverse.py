# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
# For example: if the input string is "Hello World and Coders" then your program should return the string "sredoC dna dlroW olleH"
#I did it in 2 ways, as following:

#Long way
def FirstReverse(strParam):
  to_reverse = []
  for word in strParam:
    to_reverse.append(word)
  
  to_reverse.reverse()
  reverse = ''.join(to_reverse)
  
  return reverse
  
print(FirstReverse(input()))

#Simple way
def FirstReverse2(strParam):
  return strParam[::-1]

print(FirstReverse2(input()))
