class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5
        print(f"The car accelerates. Speed is now {self.speed} mph.")

    def brake(self):
        self.speed = max(0, self.speed - 5)
        print(f"The car brakes. Speed is now {self.speed} mph.")

    def honk(self):
        print("Beep beep!")


# Create instances (objects) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

# Use the objects
car1.accelerate()  # Output: The car accelerates. Speed is now 5 mph.
car1.accelerate()  # Output: The car accelerates. Speed is now 10 mph.
car1.brake()       # Output: The car brakes. Speed is now 5 mph.
car1.honk()        # Output: Beep beep!

car2.accelerate()  # Output: The car accelerates. Speed is now 5 mph.
car2.honk()        # Output: Beep beep!
