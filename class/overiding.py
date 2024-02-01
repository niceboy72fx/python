class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Tạo đối tượng từ lớp Dog
dog = Dog()
print(dog.speak())  # Output: Dog barks

# Tạo đối tượng từ lớp Cat
cat = Cat()
print(cat.speak())  # Output: Cat meows