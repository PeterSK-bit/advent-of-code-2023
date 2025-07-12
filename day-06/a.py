with open("data.txt","r") as f:
    times = list(map(lambda x:int(x),filter(lambda x:x!="",f.readline().strip().split(" ")[1:])))
    distances = list(map(lambda x:int(x),filter(lambda x:x!="",f.readline().strip().split(" ")[1:])))
result = 1
for index,time in enumerate(times):
    temp = 0
    for speed in range(time+1):
        if speed*(time-speed) > distances[index]:
            temp+=1
    if temp != 0:
        result*=temp
print(result)