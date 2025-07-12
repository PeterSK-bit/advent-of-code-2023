with open("data.txt","r") as f:
    histories = [history.split(" ") for history in f.read().splitlines()]
    histories = [list(map(lambda x:int(x),history)) for history in histories]

sumup = 0
for history in histories:
    all_temps = []
    temp = []

    for index in range(0,len(history)-1):
        temp.append(history[index+1] - history[index])
    all_temps.append(temp)

    while all_temps[-1].count(all_temps[-1][0]) != len(all_temps[-1]):
        temp = []
        for index in range(0,len(all_temps[-1])-1):
            temp.append(all_temps[-1][index+1] - all_temps[-1][index])
        all_temps.append(temp)
    
    temp = all_temps[-1][-1]
    for index in range(len(all_temps)-2,-1,-1):
        temp += all_temps[index][-1]
    sumup+=history[-1]+temp

print(sumup)