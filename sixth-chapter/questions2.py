def add(n):
    if (n==0):
        return 0
    return add(n-1)+n

print(add(5))

name=["Neeharika", "Virat", "Shubhaman","Rahul"]

def print_list(list,index=0):
    if len(list) == index:
        return 
    print(list[index])
    print_list(list,index+1)

print_list(name,)