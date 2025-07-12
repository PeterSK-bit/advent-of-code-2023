with open("data.txt","r") as f:
    data = f.read().splitlines()
emty_rows = []
empty_columns = []
galaxies = []
sumup = 0

for y,line in enumerate(data):
    if line.count("#") == 0:
        emty_rows.append(y)
    else:
        for i in range(line.count("#")):
            galaxies.append((line.find("#"),y))
            line = line.replace("#",".",1)

for x in range(len(data[0])):
    temp = [line[x] for line in data]
    if temp.count("#") == 0:
        empty_columns.append(x)
del temp

for c,galaxy in enumerate(galaxies):
    for r in range(c+1,len(galaxies)):
        column_set = set(range(galaxy[0] if galaxy[0] < galaxies[r][0] else galaxies[r][0], (galaxy[0] if galaxy[0] > galaxies[r][0] else galaxies[r][0])+1))
        row_set = set(range(galaxy[1] if galaxy[1] < galaxies[r][1] else galaxies[r][1], (galaxy[1] if galaxy[1] > galaxies[r][1] else galaxies[r][1])+1))
        sumup += abs(galaxy[0]-galaxies[r][0]) + abs(galaxy[1]-galaxies[r][1]) + len(column_set.intersection(empty_columns)) + len(row_set.intersection(emty_rows))
print(sumup)