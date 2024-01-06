class Buyer:
    def __init__(self, name, age, money, home="Дома нет"):
        self.name = self.__check_str(name)
        self.age = self.__check_age(age)
        self.__money = self.__check_money(money)
        self.__home = home

    def __check_str(self, name):
        if type(name) != str:
            raise TypeError("Ответ должен быть представлен в виде строки")
        else:
            return name

    def __check_age(self, age):
        if type(age) != int or not 18 <= age <= 100:
            raise TypeError(
                "Возраст может быть представлен в виде целого числа от 18 до 100"
            )
        else:
            return age

    def __check_money(self, money):
        if type(money) not in (int, str):
            raise TypeError(
                "Количество денег может быть представлено в виде целого или вещественного числа"
            )
        else:
            return money

    def info(self):
        print(
            f"Покупатель: {self.name}, {self.age} лет\nБюджет и наличие дома: {self.__money}р, {self.__home}"
        )

    def buy_home(self, object):
        if self.__money >= object.price:
            self.__money = self.__money - object.price
            self.__home = f"У вас есть дом: {object.name}"
            print("Вы купили дом")
        else:
            print("Недостаточно золота для покупки дома")

    def go_work(self):
        self.__money = self.__money + 500000


class Home:
    def __init__(self, name, square, price):
        self.square = self.__check_int(square)
        self.price = self.__check_int(price)
        self.name = self.__check_str(name)

    def __check_str(self, name):
        if type(name) != str:
            raise TypeError("Ответ должен быть представлен в виде строки")
        else:
            return name

    def __check_int(self, x):
        if type(x) != int or x < 0:
            raise TypeError(
                "Площадь дома и его стоимость должны быть представлены целыми числами больше нуля"
            )
        else:
            return x

    def info_home(self):
        print(
            f"Дом {self.name} имеет площадь {self.square}, его стоимость {self.price}"
        )

    def get_discount(self):
        self.price = self.price * 0.9
        print(f"Скидка 10% на дом применена, теперь он стоит {self.price}")


nikita = Buyer("Никита", 30, 10000000)
h1 = Home("Таунхаус", 120, 5000000)
nikita.info()
h1.info_home()
h1.get_discount()
nikita.buy_home(h1)
nikita.go_work()
nikita.info()
