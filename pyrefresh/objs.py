class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (14, 43, 56, 3, 32, 85)

    def total(self):
        return sum(self.numbers)

player1 = LotteryPlayer("Josie")
player2 = LotteryPlayer("Jackie")
print(player1.name)
print(player2.name)
