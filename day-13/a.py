def read_file(file):
    temp = []
    with open(file,"r") as f:
        for line in f:
            if line != "\n":
                temp.append(line.strip())
            elif temp:
                yield temp
                temp = []
    if temp:
        yield temp

def find_reflection(array:list[str],multiplier = 1) -> int:
    result = 0
    for index in range(len(array)-1):
        if array[index] == array[index+1]:
            for i in range(1, index+1 if index+1 < len(array)-(index+1) else len(array)-(index+1)):
                if array[index-i] != array[index+1+i]:
                        break
            else:
                result += (index+1)*multiplier
                break
    return result

sumup = 0

for data in read_file("data.txt"):
    
    #horizontal
    sumup += find_reflection(data,100)

    #vertical
    #rotated data for 90 degrees to right
    sumup += find_reflection(["".join(row[i] for row in data[::-1]) for i in range(len(data[0]))])
print(sumup)