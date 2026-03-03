""" A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


"""

s = "A man, a plan, a canal: Panama"
give_str = s.lower()
reverse = ""
chars = "".join(char for char in s if char.isalnum()).lower()

print(reverse)

if reverse == s.lower():
  print(True)
  
else:
  print(False)