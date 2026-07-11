a=input("Enter a movie:")
b=input("Enter a movie:")
c=input("Enter a movie:")

movies=[]
movies.append(a)
movies.append(b)
movies.append(c)
print(movies)

list=['m','a','d','a','m']

new_list=list.copy()
new_list.reverse()

if(new_list==list):
    print("Palindrome")
else:
    print("Not Palindrome")

Grade=['A','B','A','B','C','A']
Grade.sort()
print(Grade)
print(Grade.count('A'))
