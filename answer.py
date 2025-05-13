# 1. Designing a Class
class Superhero:
    def __init__(self, name, power, health, city):
        self.name = name
        self.power = power
        self.health = health
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def take_damage(self, damage):
        self.health -= damage
        return f"{self.name} takes {damage} damage and now has {self.health} health."

    def is_alive(self):
        return self.health > 0


# Inherited class: a specialized superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, city, flight_speed):
        super().__init__(name, power, health, city)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies through {self.city} at {self.flight_speed} mph!"

    # Polymorphism: override use_power
    def use_power(self):
        return f"{self.name} swoops down and uses {self.power}!"

# Example usage:
hero1 = Superhero("Shadow Knight", "Shadow Strike", 100, "Gothica")
hero2 = FlyingSuperhero("Sky Blaze", "Flame Burst", 120, "Metro City", 300)

print(hero1.introduce())
print(hero1.use_power())
print(hero1.take_damage(20))
print(hero1.is_alive())

print(hero2.introduce())
print(hero2.fly())
print(hero2.use_power())
print(hero2.take_damage(50))



# 2. Polymorphism
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


class Bike(Vehicle):
    def move(self):
        print("Cycling 🚴")


# Demonstration of polymorphism
def vehicle_moves(vehicles):
    for vehicle in vehicles:
        vehicle.move()


# Creating instances
my_vehicles = [Car(), Plane(), Boat(), Bike()]

# Call the same method on each object
vehicle_moves(my_vehicles)
