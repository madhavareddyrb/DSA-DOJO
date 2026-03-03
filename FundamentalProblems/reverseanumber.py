# Input: x = 123
# Output: 321

# sudeo code : take remainder of x lessthan 0 with 10 to get last digit and later do string concatenation 

x = 1534236469
num =abs(x)
reverse_number = 0
sign = -1 if x < 0 else 1
  
while num > 0:
  r = num % 10
  reverse_number = reverse_number * 10 + r
  num = num // 10
  
print(reverse_number * sign)





