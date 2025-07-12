#INCOMPLETE

class Mirror:
    def __init__(self, symbol):
        self.symbol = symbol
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    def __str__(self) -> str:
        return self.symbol

    def __eq__(self, __value: str) -> bool:
        return self.symbol == __value

    def delete_direction(self, direction) -> bool:#rework!
        if direction in self.directions:
            self.directions.remove(direction)
            if self.symbol == "/":
                self.directions.remove((-direction[1],-direction[0]))
            else:
                self.directions.remove((direction[1],direction[0]))
            return True
        else:
            return False

class Splitter(Mirror):
    def delete_direction(self, direction) -> bool:
        if direction in self.directions:
            if self.directions.index(direction) > 1:
                self.directions = self.directions[:2]
            else:
                self.directions = self.directions[2:]
            return True
        else:
            return False

with open("data.txt","r") as f:
    field = [list(i) for i in f.read().splitlines()]
resoult = [[" "]*len(field[0])for _ in range(len(field))]

def ray(array:list, x:int, y:int, direction:tuple) -> None:
    resoult[y][x] = "#"
    while True:
        if x + direction[0] >= 0 and x + direction[0] < len(array[0]) and y + direction[1] >= 0 and y + direction[1] < len(array):
            x += direction[0]
            y += direction[1]
            resoult[y][x] = "#"
            if array[y][x] != ".":
                if str(array[y][x]) in "\/":
                    if isinstance(array[y][x],Mirror):
                        if array[y][x].delete_direction(direction):
                            if array[y][x] == "/":
                                ray(field, x, y, (-direction[1],-direction[0]))
                            else:
                                ray(field, x, y, (direction[1],direction[0]))

                    else:
                        array[y][x] = Mirror(array[y][x])
                        array[y][x].delete_direction(direction)
                        if array[y][x] == "/":
                            ray(field, x, y, (-direction[1],-direction[0]))
                        else:
                            ray(field, x, y, (direction[1],direction[0]))

                elif str(array[y][x]) in "|-":
                    if isinstance(array[y][x],Splitter):
                        if array[y][x].delete_direction(direction):
                            if array[y][x] == "|":
                                if direction[1] == 0:
                                    ray(field, x, y, (0,1))
                                    ray(field, x, y, (0,-1))
                                else:
                                    ray(field, x, y, direction)
                            else:
                                if direction[0] == 0:
                                    ray(field, x, y, (1,0))
                                    ray(field, x, y, (-1,0))
                                else:
                                    ray(field, x, y, direction)

                    else:
                        array[y][x] = Splitter(array[y][x])
                        array[y][x].delete_direction(direction)
                        if array[y][x] == "|":
                            if direction[1] == 0:
                                ray(field, x, y, (0,1))
                                ray(field, x, y, (0,-1))
                            else:
                                ray(field, x, y, direction)
                        else:
                            if direction[0] == 0:
                                ray(field, x, y, (1,0))
                                ray(field, x, y, (-1,0))
                            else:
                                ray(field, x, y, direction)
                break
        else:
            break

ray(field, 0, 0, (1,0))
sumup = 0
for i in resoult:
    sumup += i.count("#")
print(sumup)
#too low 5770