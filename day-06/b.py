#ignore the spaces its only one time and one distance
with open("data.txt","r") as f:
    time = int(f.readline().replace(" ", "").removeprefix("Time:"))
    distance = int(f.readline().replace(" ", "").removeprefix("Distance:"))
result = 0
for speed in range(time+1):
    if speed*(time-speed) > distance:
        result+=1
print(result)