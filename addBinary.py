# Given two binary strings a and b, return their sum as a binary string.
# Challenge available in leetcode.com

def addBinary(a: str, b: str) -> str:
   res = int(str(a),2) + int(str(b),2)
   return bin(res)[2:]
