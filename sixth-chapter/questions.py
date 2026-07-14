 #1
cities = ["Kolhapur", "Mumbai", "Solapur", "pune"]
Numbers = ["seven","one", "five"]


def print_length(list):
    print(len(list))

print_length(cities[3])
print_length(Numbers)

#2
print(Numbers[0], end=" ")
print(Numbers[1], end=" ")

def print_list(list):
    for item in list:
        print(item, end =" ")

print_list(Numbers)
print()

print_list(cities)

#3
def calc_fact(n=5):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)

calc_fact()


#4

def converter(usd_value):
    inr_value = usd_value * 83
    print(usd_value ,"USD =", inr_value , "INR")

converter(2)

#5
def to_check(a):
    if(a%2 == 0):
        print("Even")
    else:
        print("Odd")

to_check(5)
to_check(4)
    

    
