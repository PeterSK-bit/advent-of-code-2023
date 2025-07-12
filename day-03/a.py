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
numbers = []
for num in nums:
    xl = num[1]-1 if num[1]-1 >= 0 else num[1]
    xr = num[2]+1 if num[2]+1 < len(file[num[3]]) else num[2]
    passed = False
    for y in [num[3]-1,num[3],num[3]+1]:
        if y>=0 and y<len(file) and len(file[y][xl:xr].strip("0123456789.")):
            passed = True
            break
    if passed:
        numbers.append(int(num[0]))
print(sum(numbers))