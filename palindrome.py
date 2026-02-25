# Palindrome: A number or string but be same from left to right and right to left
# input = 121  , output = true

n = 121
num = n
reverse = 0

while num > 0:
  r = num % 10
  reverse =  reverse * 10 + r
  num = num // 10

# print(reverse)
# if reverse == n:
#   print(True)
# else:
#   print(False)
  
  

name = 121
input = name
store_reverse = ""

for i in input:
  
  store_reverse = i + store_reverse 

print(store_reverse)
if name == store_reverse:
  print(True)
else:
  print(False)
  
  
