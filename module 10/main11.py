class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age


S = Student("John", 25)
print("Name of Student:", S.name)
print("Age of Student:", S.age)

S.name = "Ylli"
S.age = 17

print("Updated age is:", S.age)
print("Updated name is:", S.name)
