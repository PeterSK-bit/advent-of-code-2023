with open("data.txt","r") as f:
    tseeds,*rest = f.read().split("\n\n")
tseeds = list(map(lambda x: int(x),tseeds.split(" ")[1:]))
seeds = [(tseeds[i],tseeds[i]+tseeds[i+1]) for i in range(0,len(tseeds),2)]

for part in rest:
    intervals = []
    for l in part.split("\n")[1:]:
        intervals.append(tuple(map(lambda x: int(x),l.split(" "))))
    new_seeds = []
    while seeds:
        start,end=seeds.pop()
        for start_d, start_s,increment in intervals:
            overlap_start = start if start > start_s else start_s
            overlap_end = end if end < start_s+increment else start_s+increment
            if overlap_start < overlap_end:
                new_seeds.append((overlap_start - start_s + start_d, overlap_end - start_s + start_d))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if overlap_end < end:
                    seeds.append((overlap_end, end))
                break
        else:
            new_seeds.append((start, end))
    seeds=new_seeds

min = seeds[0][0]
for x, _ in seeds:
    if x < min:
        min = x

print(min)