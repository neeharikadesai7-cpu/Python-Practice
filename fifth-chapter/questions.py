#q1

# i =1 

# while i<= 100:
#     print(i)
#     i += 1

# #q2

# i = 100

# while i>=1: #stop condition
#     print(i)
#     i -=1

#q3

# n=int(input("Enter a number:"))

# i=1
# while i<= 10:
#     print(n, "*",i, "=",n*i)
#     i += 1

#q4

# i = 1

# while i<=10:
#     print(i*i)
#     i += 1

#q5 

# num = [1, 4,9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(num):
#     print(num[i]) #nums[0], nums[1], nums[2]...
#     i += 1

#q6

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x= 36
# i = 0
# while i < len(num):
#     if num[i] ==x:
#         print("Found the number!" ,i)
#     i += 1


#q7

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for n in num:
#     print(n)

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = int(input("Enter a number to search:"))
for n in num:
    if n == x:
        print("Found the number", n , "at index", num.index(n))
        break
    else:
        print("Finding...")
        