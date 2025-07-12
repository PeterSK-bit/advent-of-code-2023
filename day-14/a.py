with open("data.txt","r") as f:
    platform = [list(i) for i in f.read().splitlines()]

def find_char(array:list, character) -> int:
    for index, char in enumerate(array):
        if char == character:
            return index
    return -1

for i in range(1,len(platform)):
    if num_of_O := platform[i].count("O"):
        checked = 0
        for o in range(num_of_O):
            x = find_char(platform[i][checked:], "O") + checked
            checked = x+1
            for j in range(i-1,-1,-1):
                if platform[j][x] in ["O","#"]:
                    platform [i][x] = "."
                    platform[j+1][x] = "O"
                    break
            else:
                platform [i][x] = "."
                platform[0][x] = "O"

sumup = 0
for index,line in enumerate(platform):
    sumup += line.count("O")*(len(platform) - index)
print(sumup)