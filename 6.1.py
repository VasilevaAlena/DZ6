class Goose1:
    weight = 6
    name = 'Gray'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def collect_eggs(self, eggs):
        self.weight -= eggs

goose_gray = Goose1()
goose_gray.shout('ga-ga-ga')
goose_gray.eat(0.3)
goose_gray.collect_eggs(0.3)
print(goose_gray.weight)


# goose_white = Farm('goose', 'White', 'ga-ga-ga', 5, 'eggs')
class Goose2:
    weight = 5
    name = 'White'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def collect_eggs(self, eggs):
        self.weight -= eggs

goose_white = Goose2()
goose_white.shout('ga-ga-ga')
goose_white.eat(0.2)
goose_white.collect_eggs(0.2)
print(goose_white.weight)


class Cow:
    weight = 157
    name = 'Manka'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def milking(self, milk):
        self.weight -= milk

cow_manka = Cow()
cow_manka.shout('muuuu')
cow_manka.eat(3)
cow_manka.milking(3)
print(cow_manka.weight)


class Sheep1:
    weight = 38
    name = 'Lamb'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def cut(self, wool):
        self.weight -= wool

sheep_lamb = Sheep1()
sheep_lamb.shout('beeeeee')
sheep_lamb.eat(1)
sheep_lamb.cut(1)
print(sheep_lamb.weight)


class Sheep2:
    weight = 35
    name = 'Curly'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def cut(self, wool):
        self.weight -= wool

sheep_curly = Sheep2()
sheep_curly.shout('beeeeee')
sheep_curly.eat(1)
sheep_curly.cut(1)
print(sheep_curly.weight)


class Chicken1:
    weight = 2
    name = 'Ko-ko'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def collect_eggs(self, eggs):
        self.weight -= eggs

chicken_ko = Chicken1()
chicken_ko.shout('ko-ko-ko')
chicken_ko.eat(0.1)
chicken_ko.collect_eggs(0.1)
print(chicken_ko.weight)


class Chicken2:
    weight = 3
    name = 'Kukareku'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def collect_eggs(self, eggs):
        self.weight -= eggs

chicken_ku = Chicken2()
chicken_ku.shout('Kukareku')
chicken_ku.eat(0.1)
chicken_ku.collect_eggs(0.1)
print(chicken_ku.weight)


class Goat1:
    weight = 22
    name = 'Horns'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def milking(self, milk):
        self.weight -= milk

goat_horns = Goat1()
goat_horns.shout('meeee')
goat_horns.eat(0.5)
goat_horns.milking(0.5)
print(goat_horns.weight)


class Goat2:
    weight = 24
    name = 'Hooves'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def milking(self, milk):
        self.weight -= milk

goat_hooves = Goat2()
goat_hooves.shout('meeee')
goat_hooves.eat(0.6)
goat_hooves.milking(0.6)
print(goat_hooves.weight)


class Duck:
    weight = 4
    name = 'Mallard'

    def shout(self, vote):
        print(f'{self.name} asked {vote}')

    def eat(self, food):
        self.weight += food

    def collect_eggs(self, eggs):
        self.weight -= eggs

duck_mallard = Duck()
duck_mallard.shout('quack-quack-quack')
duck_mallard.eat(0.2)
duck_mallard.collect_eggs(0.2)
print(duck_mallard.weight)


all_examp = [goose_gray, goose_white, cow_manka, sheep_lamb, sheep_curly, chicken_ko, chicken_ku, goat_horns, goat_hooves, duck_mallard]
all_sum = sum(farm.weight for farm in all_examp)
print(f'Weight all animals: {all_sum} kg')

max_weight = max(farm.weight for farm in all_examp)
for farm in all_examp:
    if farm.weight == max_weight:
        print(f'Weight every big animal: {max_weight} kg. It - {farm.name}')
