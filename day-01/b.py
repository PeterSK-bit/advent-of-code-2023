with open("data.txt","r") as f:
    finput = f.readlines()
nums=[]
for line in finput:
    temp = ""
    for i in range(len(line)):
        if not (line[i].isnumeric() or line[i+1].isnumeric()):
            for num in (("one","1"),("two","2"),("three","3"),("four","4"),("five","5"),("six","6"),("seven","7"),("eight","8"),("nine","9"),("zero","0")):
                if num[0] in line[i:i+5]:
                    temp += num[1]
                    break
        elif line[i].isnumeric():
            temp += line[i]
        else:
            temp += line[i+1]
        if len(temp)>0:
            break
    
    for i in range(len(line)):
        if not (line[::-1][i].isnumeric() or line[::-1][i+1].isnumeric()):
            for num in (("one","1"),("two","2"),("three","3"),("four","4"),("five","5"),("six","6"),("seven","7"),("eight","8"),("nine","9"),("zero","0")):
                if num[0] in line[::-1][i:i+5][::-1]:
                    temp += num[1]
                    break
        elif line[::-1][i].isnumeric():
            temp += line[::-1][i]
        else:
            temp += line[::-1][i+1]
        if len(temp)>1:
            break
    
    if len(temp)>1:
        nums.append(int(temp))
print(sum(nums))