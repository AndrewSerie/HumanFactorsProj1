class Box(object):
    def __init__(self, name, price, image, description):
        self.name = name
        self.price = price
        self.image = image
        self.quantity = 1
        self.addOns = []
        self.description = description
