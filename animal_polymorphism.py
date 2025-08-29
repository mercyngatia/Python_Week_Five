# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals 
# or vehicles with the same action (like move()). However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Base class Animal
class Animal:
    def move(self):
        print("This animal is moving")

# Fish sub-class
class Fish(Animal):
    def move(self):
        print("Swimming in water")

# Bird sub-class
class Bird(Animal):
    def move(self):
        print("Flying in the sky")

# Fish sub-class
class Cow(Animal):
    def move(self):
        print("Walking on land")
        
# Snake sub-class
class Snake(Animal):
    def move(self):
        print("Slithering on the ground")

# Create a list of different animals
animals = [Fish(), Bird(), Cow(), Snake()]

# Loop through each animal and call its move method
for a in animals:
    a.move()
