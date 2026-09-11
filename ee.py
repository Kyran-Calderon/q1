class Vehicle:
    def __init__(self, kindofvehicle):
        self.kindofvehicle = kindofvehicle
        print(self.kindofvehicle, "created")
    def move(self, distance):
        print(self.kindofvehicle, "moved", distance)

class Car(Vehicle):
    def __init__(self, kindofvehicle, brand, model):
        self.brand = brand
        self.model = model
        super().__init__(kindofvehicle)
        print("It is a", brand, model)
    def move(self, distance):
        super().move(distance)
        print("KM")

class Boat(Vehicle):
    def __init__(self, kindofvehicle, model):    
        self.model = model
        super().__init__(kindofvehicle)
        print("It is a", self.model)
    def move(self, distance):
        super().move(distance)
        print("Nm")

vios = Car("Car", "Toyota", "Vios")
vios.move(10)
ferry = Boat("Ferry", "Super Ferry")
ferry.move(20)
