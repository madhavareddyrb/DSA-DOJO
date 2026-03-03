'''
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

1.take 2 variables to track max, second max
2.if 

'''
list = [12, 35, 1, 10, 34, 1]
largest = 0
second =0

for i in list:
  if i > largest:
    second = largest
    largest = i
  if i > second:
    second = i
print(largest)
print(second, "sec")