class Car:
    category = "Vehicle"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"The {self.make} {self.model} has started."

    def stop(self):
        return f"The {self.make} {self.model} has stopped."

    def drive(self, distance):
        return f"The {self.make} {self.model} has driven {distance} miles."








