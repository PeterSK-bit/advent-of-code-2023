with open("data.txt","r") as f:
    file = f.readlines()
sumup = 0
for line in file:
    temp = 0
    card = list(filter(lambda x: x != "", line.split("|")[0].strip().split(" ")[2:]))
    winning_nums = list(filter(lambda x: x != "", line.split("|")[1].strip().split(" ")))
    for num in card:
        if num in winning_nums:
            temp+=1
    if temp != 0:
        sumup+=2**(temp-1)
print(sumup)