with open("data.txt","r") as f:
    file = []
    temp = ""
    for line in f.readlines():
        if line != "\n":
            temp+=line
        else:
            file.append(temp.split(":")[1].replace("\n"," "))
            temp = ""
    else:
        file.append(temp.split(":")[1].replace("\n"," "))

seeds = [int(i) for i in file[0].strip().split(" ")]
soil,fertilizer,water,light,temperature,humidity,location = [],[],[],[],[],[],[]
for index,item in enumerate([soil,fertilizer,water,light,temperature,humidity,location]): item.extend([[int(i) for i in file[index+1].strip().split(" ")[i:i+3]] for i in range(0,len(file[index+1].strip().split(" ")),3)])

seeds_location = []
for seed in seeds:
    for item in [soil,fertilizer,water,light,temperature,humidity,location]:
        for i in item:
            if seed in range(i[1],i[1]+i[2]):
                seed = i[0]+(seed-i[1])
                break
    seeds_location.append(seed)
print(min(seeds_location))