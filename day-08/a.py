with open("data.txt","r") as f:
    file = f.readlines()
    instructions = file[0].strip()
    map_ = [i.strip(")\n").replace(" = (",", ").split(", ") for i in file[2:]]

for item in map_:
    if item[0] == "AAA":
        position = item
        break
index = 0

while position[0] != "ZZZ":
    if instructions[index % len(instructions)] == "L":
        for item in map_:
            if item[0] == position[1]:
                position = item
                index += 1
                break
    else:
        for item in map_:
            if item[0] == position[2]:
                position = item
                index += 1
                break
print(index)