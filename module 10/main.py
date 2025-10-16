class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age


student1 = Student("John", 25)

print(student1.get_name())
student1.set_name("Joni")
print("Updated name is:", student1.get_name())
print("Updated age is:", student1.get_age())
student1.set_age(25)
print("Updated age is:", student1.get_age())