class Farm:

    def __init__(self, name, nickname, vote, weight, action):
        self.name = name
        self.nickname = nickname
        self.vote = vote
        self.weight = weight
        self.action = action

    def eat(self, food):
        self.weight += food

    def cut(self, wool):
        self.weight -= wool

    def collect_eggs(self, eggs):
        self.weight -= eggs

    def milking(self, milk):
        self.weight -= milk

goose_gray = Farm('goose', 'Gray', 'ga-ga-ga', 6, 'eggs')
goose_white = Farm('goose', 'White', 'ga-ga-ga', 5, 'eggs')
cow_manka = Farm('cow', 'Manka', 'muuuu', 157, 'milk')
sheep_lamb = Farm('sheep', 'Lamb', 'beeeeee', 38, 'wool')
sheep_curly = Farm('sheep', 'Curly', 'beeeeee', 35, 'wool')
chicken_ko = Farm('chicken', 'Ko-ko', 'ko-ko-ko', 1, 'eggs')
chicken_ku = Farm('chicken', 'Kukareku', 'Kukareku', 2, 'eggs')
goat_horns = Farm('goat', 'Horns', 'meeee', 22, 'milk')
goat_hooves = Farm('goat', 'Hooves', 'meeee', 24, 'milk')
duck_mallard = Farm('duck', 'Mallard', 'quack-quack-quack', 3, 'eggs')

print(goose_gray.vote)
goose_gray.eat(0.2)
print(goose_gray.weight)
goose_gray.collect_eggs(0.2)
print(goose_gray.weight)

print(goose_white.vote)
goose_white.eat(0.2)
print(goose_white.weight)
goose_white.collect_eggs(0.2)
print(goose_white.weight)

print(cow_manka.vote)
cow_manka.eat(2)
print(cow_manka.weight)
cow_manka.milking(2)
print(cow_manka.weight)

print(sheep_lamb.vote)
sheep_lamb.eat(1.3)
print(sheep_lamb.weight)
sheep_lamb.cut(1.8)
print(sheep_lamb.weight)

print(sheep_curly.vote)
sheep_curly.eat(0.7)
print(sheep_curly.weight)
sheep_curly.cut(1.5)
print(sheep_curly.weight)

print(chicken_ko.vote)
chicken_ko.eat(0.1)
print(chicken_ko.weight)
chicken_ko.collect_eggs(0.1)
print(chicken_ko.weight)

print(chicken_ku.vote)
chicken_ku.eat(0.1)
print(chicken_ku.weight)
chicken_ku.collect_eggs(0.1)
print(chicken_ku.weight)

print(goat_horns.vote)
goat_horns.eat(0.7)
print(goat_horns.weight)
goat_horns.milking(1)
print(goat_horns.weight)

print(goat_hooves.vote)
goat_hooves.eat(0.4)
print(goat_hooves.weight)
goat_hooves.milking(0.4)
print(goat_hooves.weight)

print(duck_mallard.vote)
duck_mallard.eat(0.2)
print(duck_mallard.weight)
duck_mallard.collect_eggs(0.2)
print(duck_mallard.weight)

all_examp = [goose_gray, goose_white, cow_manka, sheep_lamb, sheep_curly, chicken_ko, chicken_ku, goat_horns, goat_hooves, duck_mallard]
all_sum = sum(Farm.weight for Farm in all_examp)
print(f'Общий вес всех животных после еды и ухода: {all_sum} кг')

max_weight = max(Farm.weight for Farm in all_examp)
for Farm in all_examp:
    if Farm.weight == max_weight:
        print(f'Вес самого большого животного: {max_weight} кг. Это - {Farm.name}, по прозвищу {Farm.nickname}')
