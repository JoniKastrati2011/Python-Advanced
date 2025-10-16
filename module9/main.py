# class Superclass:
#
#     class Subclass(Superclass):
#
#

class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def sound(self):
        print("Animal is sounding")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
#     def eat(self):
#         print("Dog is eating")


class Cat(Animal):
    def sound(self):
        print("Cat is sounding")

class Dog(Animal):
    def sound(self):
        print("Dog is sounding")

animal = Animal()
animal.sound()

cat = Cat()
cat.sound()
dog = Dog()
dog.sound()