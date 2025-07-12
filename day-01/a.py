with open("data.txt","r") as f:
    finput = f.readlines()
nums = []
for line in finput:
    num = ""
    for char in line:
        if char.isnumeric():
            num+=char
            break
    for char in line[::-1]:
        if char.isnumeric():
            num+=char
            break
    nums.append(int(num))
print(sum(nums))