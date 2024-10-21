
class Item:     # Item class that's a parent for all others
    def __init__(self, id, name, price, img):
        self.id = id
        self.name = name
        self.price = price
        self.img = img


class Shirts(Item):     # inherits Item's attributes
    def __init__(self, id, name, price, img):
        super().__init__(id, name, price, img)


class Accessories(Item):
    def __init__(self, id, name, price, img):
        super().__init__(id, name, price, img)


class Jeans(Item):
    def __init__(self, id, name, price, img):
        super().__init__(id, name, price, img)


class Trousers(Item):
    def __init__(self, id, name, price, img):
        super().__init__(id, name, price, img)
