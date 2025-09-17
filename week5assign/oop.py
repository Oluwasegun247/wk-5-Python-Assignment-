
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")



phone = Smartphone("Techno", "Smart8", 246)

phone.info()


phone.call("+2348067833673")


class Gamingphone(Smartphone):
    def __init__(self, brand, model, storage, gpu_power):
        super().__init__(brand, model, storage)
        self.__gpu_power = gpu_power

    def play_game(self, game):
        print(f"Playing {game} with GPU power {self.__gpu_power}..")


gaming = Gamingphone("Asus", "ROG 6", 512, "High-End GPU")

gaming.info()
gaming.play_game("DL25, Dream League")


# The Polymorphism
class Vehicle:
    def move(self):
        print("The Vehicle is Moving")


class Car(Vehicle):
    def move(self):
        print("Driving.......")



class ship(Vehicle):
    def move(self):
        print("Sailing.......")
        

class plane(Vehicle):
    def move(self):
        print("Flying.......")


Vehicle = [Car(),ship(),plane()]

for v in Vehicle:
    v.move()