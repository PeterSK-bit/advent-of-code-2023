class Hand:
    def __init__(self,cards:str,value:int) -> None:
        self.cards = cards
        self.value = value
        self.type = self.type_setter()
    cards_values_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    type_values_order = ["five of a kind","four of a kind","full house","three of a kind","two pairs","pair","high card"]
    
    def __gt__(self,other):
        if self.type_values_order.index(self.type) < self.type_values_order.index(other.type):
            return True
        elif self.type == other.type:
            for index in range(len(self.cards)):
                if self.cards_values_order.index(self.cards[index]) != self.cards_values_order.index(other.cards[index]):
                    if self.cards_values_order.index(self.cards[index]) < self.cards_values_order.index(other.cards[index]):
                        return True
                    if self.cards_values_order.index(self.cards[index]) > self.cards_values_order.index(other.cards[index]):
                        return False
        return False

    def cards_sort(self,hand:str) -> str:
        return "".join(i for i in sorted(hand,key=lambda x:self.cards_values_order.index(x)))

    def type_setter(self):
        temp = self.cards_sort(self.cards)
        if temp.count(temp[2]) == 5:
            return "five of a kind"
        elif temp.count(temp[2]) == 4:
            return "four of a kind"
        elif temp.count(temp[2]) == 3:
            if temp.count(temp[0]) == 2 or temp.count(temp[4]) == 2:
                return "full house"
            else:
                return "three of a kind"
        elif temp.count(temp[1]) == 2 and temp.count(temp[3]) == 2:
            return "two pairs"
        elif temp.count(temp[1]) == 2 or temp.count(temp[3]) == 2:
            return "pair"
        else:
            return "high card"

with open("data.txt","r") as f:
    hands = [Hand(i.strip().split(" ")[0],int(i.strip().split(" ")[1])) for i in f.readlines()]

hands.sort()
for i in hands: print(i.cards,i.type)
sumup = 0
for index,hand in enumerate(hands):
    sumup+=(hand.value*(index+1))
print(sumup)