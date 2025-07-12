with open("data.txt","r") as f:
    file = f.readlines()

cards = []
winning_nums = []
sumup = 0

for line in file:
    cards.append([1,list(filter(lambda x: x != "", line.split("|")[0].strip().split(" ")[2:]))])
    winning_nums.append(list(filter(lambda x: x != "", line.split("|")[1].strip().split(" "))))

for index,card in enumerate(cards):
    temp=0
    for num in card[1]:
        if num in winning_nums[index]:
            temp+=1
    for i in range(1,temp+1):
        if index+i < len(file):
            cards[index+i][0]+=1*card[0]
        else:
            break

for card in cards:
    sumup+=card[0]
print(sumup)