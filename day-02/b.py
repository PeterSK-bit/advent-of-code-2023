# add ";" or "newline" at the end of the file
with open("data.txt","r") as f:
    finput = f.readlines()
sumup = 0
for game in finput:
    R,G,B = 0,0,0
    rgb = (["red",0],["green",0],["blue",0])
    game = game.split(" ")[2:]
    for index in range(1,len(game),2):
        for color in rgb:
            if color[0] in game[index]:
                color[1] += int(game[index-1])
                if game[index].count(";") > 0 or game[index].count("\n") > 0:
                    if rgb[0][1] > R:
                        R = rgb[0][1]
                    if rgb[1][1] > G:
                        G = rgb[1][1]
                    if rgb[2][1] > B:
                        B = rgb[2][1]                        
                    rgb = (["red",0],["green",0],["blue",0])
                    break
    sumup += R*G*B

print(sumup)