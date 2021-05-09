import random


class Dice:
    def __init__(self, count):
        self.count = count
        self.sides = [1,2,3,4,5,6]

    def roll(self):
        self.rezult = []
        for dice_X in range(self.count):
            self.rezult.append(random.choice(self.sides))
        return self.rezult


if __name__ == '__main__':
    dice = Dice(5)
    print(dice.roll())
