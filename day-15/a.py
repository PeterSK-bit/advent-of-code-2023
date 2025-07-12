with open("data.txt","r") as f:
    data = f.read().split(",")
sumup = 0
for string in data:
    temp = 0
    for char in string: 
        temp = (temp+ord(char))*17%256   
    sumup += temp
print(sumup)