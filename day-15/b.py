with open("data.txt","r") as f:
    data = f.read().split(",")

boxes = [{} for i in range(256)]
sumup = 0

for string in data:
    temp = 0
    index = string.find("=") if string.find("=") != -1 else string.find("-")
    substring = string[:index]
    for char in substring:
        temp = (temp+ord(char))*17%256 

    if string[index] == "=":
        boxes[temp].update({substring : string[index+1]})
    else:
        boxes[temp].pop(substring, None)

for index,box in enumerate(boxes):
    for slot,item in enumerate(box.values()):
        sumup += (index+1)*(slot+1)*int(item)
print(sumup)