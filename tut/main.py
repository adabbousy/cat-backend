import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=1):
        assert quantity >= 0, "Invalid quantity"
        assert price >= 0, "Invalid price"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
        
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def increase_price(self, value):
        self.__price += self.__price * value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


class Phone(Item):
    pay_rate = 0.9
    def __init__(self, name: str, price: float, quantity=1, broken_phones=0):
        assert broken_phones >= 0, "Invalid broken phones"

        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones


i = Phone("Phone", 100, 3)
i.apply_discount()
print(i.price)