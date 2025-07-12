from math import lcm

with open("data.txt","r") as f:
    file = f.read().splitlines()
    instructions = file[0]
    input_map = {}
    [input_map.update({line.split(" = (")[0]:line.split(" = (")[1].strip(")").split(", ")}) for line in file[2:]]

positions = [item for item in input_map if "A" in item]
nums = []

for index,position in enumerate(positions):
    num = 0
    while "Z" not in position:
        if instructions[num%len(instructions)] == "L":
            position = input_map[position][0]
        else:
            position = input_map[position][1]
        num += 1
    nums.append(num)
print(nums)
print(lcm(*nums))