## Maximum conscutive count of 1 and 0 o only 

list = [1,1,1,0,0,0,1,1,0,1]
count = 0
ans = 0

for i in list:
  if i > 0:
    count += 1
    ans = max(ans, count)
  else:
    count = 0
    
print(ans)