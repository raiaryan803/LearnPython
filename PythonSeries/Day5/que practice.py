#  sum of total numbers .........

n = 5

sum = 0
for i in range (1, n+1):
    sum += i

print("total sum =", sum)

#  same que using while loop se....

n = 8

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum =", sum)

#  factorial program......using while loop

n = 5

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial =", fact)

#  factorial using for loop.....

n = 8
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)

 
#   using for & range......

for i in range(1 , 101):
    print (i)

#  100 to 1...
    for i in range(100 , 0, -1):
        print (i)

# multiplication table of a number n.....
        
        n = int(input("enter number : "))

        for i in range(1, 11):
            print(n * i)