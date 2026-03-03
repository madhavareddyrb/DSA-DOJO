# # prices = [7,1,5,3,6,4]
# prices = [7,6,5,4,2,1]

# max_p = 0 # i-j = max_p 
# min_v = 10 ** 5
# for i in range(0,len(prices)):
#   for j in range(1, len(prices)):
#     if min_v > i:  # 0 < 7   7<6
      
#       min_v = i   # true minV= 7 false
#     max_p = max(max_p, (prices[j] -prices[i]))
#     # if prices[i] < prices[j]:   # 7 < 1  1 < 5   1< 3   1< 6
#     #   profit = prices[j] - prices[i]  # 5 -1 = 4  3-1 = 2  5
      
#     #   if profit > max_p :      # 4 > 0  2> 4  5>4
#     #     max_p = profit         # 4  5



prices = [7,6,5,1]
max_p = 0
min_v = float("inf")
for i in range(len(prices)):
  min_v = min(min_v, prices[i])
  
  max_p = max(max_p, prices[i]-min_v)
print(max_p)