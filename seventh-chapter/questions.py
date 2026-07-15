# #1

# with open("practice.py","w") as f:
#     f.write(" Hi everyone \n  We are learning Python \n And i am on last second chapter \n I like programming in Python")

# #2
# with open("practice.py", "r") as f:
#     data=f.read()

# new_data = data.replace("Python" , "Java")
# print(new_data)

# with open("practice.py", "w") as f:
#     f.write(new_data)

#3
word = "learning"

with open("practice.py" , "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")