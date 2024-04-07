#  function defenation....
# def calc_sum (a, b): # parameters
#     return a + b

# sum = calc_sum(966, 65)  #function call , arguments
# print (sum)

# # average of 3 numbers.......

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print (avg)
#     return avg

# calc_avg(98, 97, 95)

# # ......print function....

# print ("apnacollege", end=" ") 
# print ("shradhakhapra")

# # .........

# print ("apnacollege", end=" $ ")
# print ("shradhakhapra")

# print lenth of list...

# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
# heroes = ["thor", "ironman", "captain america", "shaktiman"]

# def print_len(list):
#     print(len(list))

#     print_len(cities)
#     print_len(heroes)
    
    # ...........

# n = 5
# fact = 1
# for i in range (1, n+1 ):
#     fact *= i
# print (fact) 

# .....fuctorial logic use for function....

# def cal_fact(n):
#     fact = 1
#     for i in  range (1, n+1):
#         fact *= i
#     print (fact) 

# cal_fact (10)    

# convert usd to inr......
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"usd =", inr_val, "inr")

converter(10)