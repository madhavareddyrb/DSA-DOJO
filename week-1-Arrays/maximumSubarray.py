'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:


Steps:
2 variables 1.max_sum 
1.check sum of list items one with one
2.take i and j for inside loop
3.not less than 0
4.i+j sum chesthu untadi and output just sum chalu
5.




Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104'''


# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]
          
sum = 0
max_sum = float("-inf")
for i in range(len(nums)):
  sum += nums[i]
  max_sum = max(max_sum,sum)
  if sum < 0:
    sum = 0
  
  # sum = 0
  # for j in range(i ,len(nums)):
  #   sum += nums[j]
  #   max_sum = max(sum, max_sum)
   
print(max_sum)