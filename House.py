class Buyer:
    def __init__(self, name = 'Иван', age = 25, money, home):
        self.name = self.check_str(name)
        self.age = self.check_age(age)
        self.__money = self.check_money(money)
        self.__home = self.check_str(home)
    def check_str(self, name):
        if type(name) != str:
            raise TypeError('Ответ должен быть представлен в виде строки')
        else:
            return name
    def check_age(self, age):
        if type(age) != int or 18 <= age <=100:
            raise TypeError('Возраст может быть представлен в виде целого числа от 18 до 100')
        else:
            return age
    def check_money(self, money):
        if type(money) not in (int, str):
            raise TypeError('Количество денег может быть представлено в виде целого или вещественного числа')
        else:
            return money

