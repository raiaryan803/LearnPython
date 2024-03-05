# print number from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#     #print number from 100 to 1..

# i = 100
# while i >= 1:  # stopping condition
#     print(i)
#     i -= 1

#     # print multiplication table of a number n......

# i = 1
# while i <= 10:
#     print(4*i)   
#     i += 1 

    # input lekar.....

# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#      print(n*i)
#      i += 1

# que4.....
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(idx)
#     idx += 1

    # .......

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# .............traverse...............

# heroes = ["guru ", "ironman", "thor", "batman", ]
# idx = 0
# while idx < len(heroes):
#      print(heroes[idx])
#      idx += 1

#  que 5....

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

# x = 36

# i = 0
# while i < len(nums):
#     if(nums[i] == x):

#         print("found at idx", i)
#         break
#     else:
#         print("finding..")
#         i += 1

#         print("end of loop")

        
#  break and countiniue .... keyword uses..........

# i = 1 
# while i <= 5:
#     print(i)
#     if(i== 3):
#         break
#     i += 1

#     #  ....

#     i = 0 
#     while i <= 5:
#         if(i == 3):
#             i += 1
#             continue # skip
#         print(i)
#         i += 1

# .........
i = 1
while i <= 10:
     if(i%2 == 0):
            i += 1
            continue # skip
     print(i)
     i += 1

    #  even no. print krane ke liye........
     
i = 1
while i <= 10:
     if(i%2 != 0):
            i += 1
            continue # skip
     print(i)
     i += 1     