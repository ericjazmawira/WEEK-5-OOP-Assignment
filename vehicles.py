class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("The Plane is flying in the sky ✈")

class Boat(Vehicle):
    def move(self):
        print("The Boat is sailing on the water 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("The Bicycle is pedalling along 🚲")

def Vehicle_action(Vehicle):
    Vehicle.move()

vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    Vehicle_action(vehicle)