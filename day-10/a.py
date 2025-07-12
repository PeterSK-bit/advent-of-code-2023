with open("data.txt","r") as f:
    field = f.read().splitlines()
#finding S
for y,line in enumerate(field):
    if "S" in line:
        start = (line.find("S"),y)

position = list(start)
if position[1]-1 > 0 and field[position[1]-1][position[0]] in ["|", "7", "F"]:
    facing = "up"
elif position[1]+1 > 0 and field[position[1]+1][position[0]] in ["|", "J", "L"]:
    facing = "down"

steps = 0

while facing != "end":
    steps += 1
    if facing == "up":
        position[1] -= 1
        if field[position[1]][position[0]] == "|":
            facing = "up"
        elif field[position[1]][position[0]] == "7":
            facing = "left"
        elif field[position[1]][position[0]] == "F":
            facing = "right"
        else:
            facing = "end"
        continue

    if facing == "down":
        position[1] += 1
        if field[position[1]][position[0]] == "|":
            facing = "down"
        elif field[position[1]][position[0]] == "L":
            facing = "right"
        elif field[position[1]][position[0]] == "J":
            facing = "left"
        else:
            facing = "end"
        continue

    if facing == "right":
        position[0] += 1
        if field[position[1]][position[0]] == "J":
            facing = "up"
        elif field[position[1]][position[0]] == "7":
            facing = "down"
        elif field[position[1]][position[0]] == "-":
            facing = "right"
        else:
            facing = "end"
        continue

    if facing == "left":
        position[0] -= 1
        if field[position[1]][position[0]] == "L":
            facing = "up"
        elif field[position[1]][position[0]] == "-":
            facing = "left"
        elif field[position[1]][position[0]] == "F":
            facing = "down"
        else:
            facing = "end"
        continue
print(f"position: {position}\nsteps: {steps//2}")