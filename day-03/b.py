with open("data.txt","r") as f:
    file = f.readlines()

nums = []
for y,line in enumerate(file):
    for x,char in enumerate(line):
        if char.isnumeric():
            if nums and nums[-1][2] == x:
                nums[-1][2]+=1
                nums[-1][0]+=char
            else:
                nums.append([char,x,x+1,y])
result = 0
for y,line in enumerate(file):
    for x,char in enumerate(line):
        if char == "*":
            temp = []
            for num in nums:
                if (num[3] >= y-1 and num[3] <= y+1) and ((num[1] >= x-1 and num[1] <= x+1) or (num[2]-1 >= x-1 and num[2]-1 <= x+1)):
                    temp.append(int(num[0]))
            if len(temp) == 2:       
                result+=temp[0]*temp[1]
print(result)