class Iterator:
    peolpe = [
        {"name": "Nikita", "age": 25},
        {"name": "Oleg", "age": 30},
        {"name": "Vasya", "age": 20},
    ]

    def __init__(self, step, start):
        self.check(step, start)
        self.step = step
        self.start = start

    def check(self, *args):
        z = list(map(lambda x: isinstance(x, int) and 0 <= x < len(self.peolpe), args))
        if not all(z):
            raise TypeError(
                "Шаг и точку старта могут обозначать только целые числа, причем их значения могут быть от 0 до длины списка"
            )
        else:
            return True

    def __iter__(self):
        self.f = -self.step
        return self

    def __next__(self):
        if self.f < len(self.peolpe) - self.step:
            self.f += self.step
            return self.peolpe[self.f]
        else:
            raise StopIteration


p1 = Iterator(1, 0)
for i in p1:
    print(i)
print(*p1)
