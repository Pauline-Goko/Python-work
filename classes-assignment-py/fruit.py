class Fruit:
    category = "Food"

    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def ripen(self, days):
        return f"The {self.name} will be ripe in {days} days."

    def eat(self):
        return f"You eat the {self.name} and it tastes {self.taste}."

    def describe(self):
        return f"The {self.name} is {self.color} in color and tastes {self.taste}."





