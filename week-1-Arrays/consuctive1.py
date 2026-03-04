nums = [1,0,1,1,0,1]
count = 0
ans = 0
for i in nums:
  if i == 1:
    count += 1
  if i == 0:
    count = 0
  ans = max(ans,count)
    
print(ans, "ans")