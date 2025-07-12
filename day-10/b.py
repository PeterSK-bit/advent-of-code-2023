#INCOMPLETE

with open("data.txt","r") as f:
    field = f.read().splitlines()

pipes = {
    "|":["up","down"],
    "L":["up","right"],
    "J":["left","up"],
    "-":["left","right"],
    "7":["left","down"],
    "F":["down","right"]
}

for y,line in enumerate(field):
    if "S" in line:
        start = (line.find("S"),y)

position = list(start)
facing = ""
moves = 0
while facing != "end":
    moves += 1
    if position[1]-1 >= 0 and facing != "down" and field[position[1]-1][position[0]] in ["|", "7", "F"]:
        facing = "up"
        position[1]-=1
    elif position[1]+1 < len(field) and facing != "up" and field[position[1]+1][position[0]] in ["|", "J", "L"]:
        facing = "down"
        position[1]+=1
    elif position[0]-1 >= 0 and facing != "right" and field[position[1]][position[0]-1] in ["L", "-", "F"]:
        facing = "left"
        position[0]-=1
    elif position[0]+1 < len(field[0]) and facing != "left" and field[position[1]][position[0]+1] in ["-", "J", "7"]:
        facing = "right"
        position[0]+=1
    else: facing = "end"
print(moves//2)