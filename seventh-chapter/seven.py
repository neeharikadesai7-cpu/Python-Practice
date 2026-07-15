with  open("dem.txt" , "r") as f:
    line1 = f.readline()
    print(line1)

    line2= f.readline()
    print(line2)
    

    print(type(line1))

f= open("sample.txt" , "w")
f.close()

with open("dem.txt","r+") as f:

    f.write("abc")
    f.close()

import os
os.remove("sample.txt")