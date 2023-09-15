class Fruit:

    def __init__(self, name, size, origin, price):
        self.name = name
        self.size = size
        self.origin = origin
        self.price = price

    def get_name(self):
        return self.name

    def get_origin(self):
        return self.origin

    def get_price(self):
        return self.price

    def juicy(self):
        return f'It is a juicy {self.name}!'

    def set_name(self, new_name):
        self.name = new_name

    sizes = []
    def add_size(self, size):
        self.sizes.append(size)

# подклассы
class Pear(Fruit):
    def __init__(self, name, size, origin, price):
        super().__init__(name, size, origin, price)

    __color = "green"

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Apple(Fruit):
    def __init__(self, name, size, origin, price):
        super().__init__(name, size, origin, price)

    __color = "red"   # private
    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

fruit_1 = Fruit('banana', 'small', 'Spain', 35)
pear1 = Pear('pear', 'large', 'France', 50)
apple1 = Apple('apple', 'meduim', 'Italy', 80)

print(pear1.get_name())
print(apple1.get_origin())
print(pear1.get_color())    # private
print(apple1.get_color())
pear1.set_color("orange")
print(pear1.get_color())
print(pear1.juicy())
print(apple1.juicy())

print(fruit_1.juicy())
print(fruit_1.get_price())

Fruit.add_size(fruit_1,'small')
fruit_1.set_name('baby banana')
print(fruit_1.juicy())
print(fruit_1.sizes)
print(Fruit.sizes)
