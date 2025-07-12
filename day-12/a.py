#INCOMPLETE

with open("data.txt","r") as f:
    data = [[list(line.split(" ")[0]),list(map(lambda x: int(x), line.split(" ")[1].strip().split(",")))] for line in f.readlines()]

def locate_broken_spings(springs: list[chr], broken_springs: int):
    for index in range(0,len(springs)-broken_springs):
        temp = springs[index:index+broken_springs]
        if temp.count("#")+temp.count("?") == broken_springs:
            if index-1 >= 0:
                if springs[index-1] == "#":
                    continue
            if index+broken_springs+1 < len(springs):
                if springs[index+broken_springs+1] == "#":
                    continue
            return index
    return -1
print(locate_broken_spings(['?', '?', '?', '.', '#', '#', '#'],1))
for map_, info in data:
    pass