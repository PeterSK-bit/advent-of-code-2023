#INCOMPLETE

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

class WrongParameters(Exception):
    pass

def two_strings_differences(line1:str, line2:str) -> int:
    if len(line1) != len(line2):
        raise WrongParameters("strings have different lengths")
    
    if line1 == line2:
        return 0

    diff = 0
    for char1, char2 in zip(line1,line2):
        if char1 != char2:
            diff += 1
    return diff

def find_reflection(array:list[str],multiplier = 1) -> int:
    result = 0
    for index in range(len(array)-1):
        diff = two_strings_differences(array[index],array[index+1])
        if diff < 2:
            array[index] = array[index+1]
            for i in range(1, index+1 if index+1 < len(array)-(index+1) else len(array)-(index+1)):
                if array[index-i] != array[index+1+i]:
                    break
            else:
                result += (index+1)*multiplier
                break
    return result

sumup = 0

for data in read_file("13.txt"):
    #horizontal
        sumup += find_reflection(data,100)

    #vertical
    #rotated data for 90 degrees to right
        sumup += find_reflection(["".join(row[i] for row in data[::-1]) for i in range(len(data[0]))])
print(sumup)
#too high 28891