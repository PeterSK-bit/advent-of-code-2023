#INCOMPLETE

with open("data.txt","r") as f:
    city = [[int(i) for i in line] for line in f.read().splitlines()]

for block in city:
    print(block)