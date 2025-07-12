with open("data.txt","r") as f:
    finput = f.readlines()
R,G,B = 12,13,14
sumup = 0
for game in finput:
    possible = True
    rgb = (["red",0],["green",0],["blue",0])
    id = game.split(" ")[1].removesuffix(":")
    game = game.split(" ")[2:]
    for index in range(1,len(game),2):
        if possible == False:
            break
        for color in rgb:
            if color[0] in game[index]:
                color[1] += int(game[index-1])
                if game[index].count(";") > 0 or game[index].count("\n") > 0:
                    if not(rgb[0][1] <= R and rgb[1][1] <= G and rgb[2][1] <= B):
                        possible = False
                    rgb = (["red",0],["green",0],["blue",0])
                    break
    if possible:
        sumup += int(id)

print(sumup)