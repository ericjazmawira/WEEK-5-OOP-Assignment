# Class goat
class Goat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.__hunger_level = 5  # Private attribute (0 = full, 10 = starving)


    def eat(self, food = "grass"):
        if self.__hunger_level > 0:
            self.__hunger_level -= 1
            print(f"{self.name} is eating {food}. Hunger level: {self.__hunger_level}")
        else:
            print(f"{self.name} is not hungry and don't want to eat {food}.")
    def bleat(self):
        print(f"{self.name} says: Maaaa!")

    def get_status(self):
        print(f"{self.name} is a {self.age} -year -old {self.breed} goat")

    def hunger_status(self):
        if self.__hunger_level >= 7:
            print(f"{self.name} is starving!")
        elif self.__hunger_level <= 2:
            print(f"{self.name} is full!")
        else:
                print (f"{self.name} could use a snack😂")

# Subclass: MountainGoat
class MountainGoat(Goat):
        def __init__(self, name, age, breed, mountain_range):
            super().__init__(name, age, breed)
            self.mountain_range = mountain_range

        def climb(self):
            print(f"{self.name} can climb over 25km uphill of the {self.mountain_range}")


        # polymorphism

        def bleat(self):
            print(f"{self.name} the mountain goat screams: 'Baaaa'!")

regular_goat = Goat("Billy", 5, "Angora")
regular_goat.get_status()
regular_goat.bleat()
regular_goat.eat()
regular_goat.hunger_status()

print("\n")
mountain_goat = MountainGoat("Misty", 3, "Tibetan", "Himalayas")
mountain_goat.get_status()
mountain_goat.bleat()
mountain_goat.climb()
mountain_goat.eat("thorny shrubs")
mountain_goat.hunger_status()