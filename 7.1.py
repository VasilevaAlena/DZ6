class Farm:

    def __init__(self, name, nickname, vote, weight):
        self.name = name
        self.nickname = nickname
        self.vote = vote
        self.weight = weight

    def eat(self, food):
        self.weight += food
        print(f'Weight {self.nickname} after eating made - {self.weight} kg')

    def sound(self):
        print(f'{self.name} {self.nickname} makes a sound "{self.vote}"')


class WoolQiving(Farm):

    def __init__(self, name, nickname, vote, weight):
        Farm.__init__(self, name, nickname, vote, weight)
        print(f'Creation WoolQiving - {self.name} {self.nickname}')

    def cut(self, wool):
        self.weight -= wool
        print(self.weight)


class EggQiving(Farm):

    def __init__(self, name, nickname, vote, weight):
        Farm.__init__(self, name, nickname, vote, weight)
        print(f'Creation EggQiving - {self.name} {self.nickname}')

    def collect_eggs(self, eggs):
        self.weight -= eggs
        print(self.weight)


class MilkQiving(Farm):

    def __init__(self, name, nickname, vote, weight):
        Farm.__init__(self, name, nickname, vote, weight)
        print(f'Creation MilkQiving - {self.name} {self.nickname}')

    def milking(self, milk):
        self.weight -= milk
        print(self.weight)

sheep_lamb = WoolQiving('sheep', 'Lamb', 'beeeeee', 38)
sheep_curly = WoolQiving('sheep', 'Curly', 'beeeeee', 35)
goose_gray = EggQiving('goose', 'Gray', 'ga-ga-ga', 6)
goose_white = EggQiving('goose', 'White', 'ga-ga-ga', 5)
chicken_ko = EggQiving('chicken', 'Ko-ko', 'ko-ko-ko', 1)
chicken_ku = EggQiving('chicken', 'Kukareku', 'Kukareku', 2)
duck_mallard = EggQiving('duck', 'Mallard', 'quack-quack-quack', 3)
cow_manka = MilkQiving('cow', 'Manka', 'muuuu', 157)
goat_horns = MilkQiving('goat', 'Horns', 'meeee', 22)
goat_hooves = MilkQiving('goat', 'Hooves', 'meeee', 24)


all_examp = [goose_gray, goose_white, cow_manka, sheep_lamb, sheep_curly, chicken_ko, chicken_ku, goat_horns, goat_hooves, duck_mallard]
for examp in all_examp:
    examp.sound()
    examp.eat(examp.weight / 10)

all_sum = sum(Farm.weight for Farm in all_examp)
print(f'Weight all animals after eating made: {all_sum} kg')

max_weight = max(Farm.weight for Farm in all_examp)
for Farm in all_examp:
    if Farm.weight == max_weight:
        print(f'Weight every big animal: {max_weight} kg. It - {Farm.name} {Farm.nickname}')
