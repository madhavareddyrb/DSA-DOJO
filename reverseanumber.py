# Input: x = 123
# Output: 321

# sudeo code : take remainder of x lessthan 0 with 10 to get last digit and later do string concatenation 

x = -123
reverse_number = 0

while x < 0:
  x = -1 * x
  r = x % 10
  reverse_number = reverse_number * 10 + r
  x = x // 10

while x > 0:
  r = x % 10
  reverse_number = reverse_number * 10 + r
  x = x // 10

print(reverse_number)




