# def calculate_area(length, width):
#     return length * width
#
# def calculate_volume(length, width):
#     return 2 * (length + width)
#
# length = 5
# width = 3
#
# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
#
# print(f'Area of perimeter: {area}')
# print(f'Perimeter of area: {perimeter}')


# class Rectangle:
#     def__init__(self , length , width):
#     self.length = length_hint
#     self.width = width
#
# def calculate_area(self):
#     return self.length + self.width
# def calculate_perimeter(self):
#     return self.length + self.width
#
# myRectangle = Rectangle(10, 10)
#
# area = my_rectangle.calculate_area()
# perimeter = my_rectangle.calculate_perimeter()
#
# print(f"area:{area}")
# print(f"perimeter:{perimeter}")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Hello, my name is " + self.name)
#
# person1 = Person("John", 20)
# person2 = Person("Joni", 14)
#
# person1.greet()
# person2.greet()

# class Student:
#     school_name = 'Digital School'
#
# student1 = Student()
# print(student1.school_name)

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
# student1 = Student("John", 21, "Python")
# student2 = Student("John", 21, "Python")
#
# print(student1.course)
# print(student2.course)

# class MyClass:
#     def __init__(self):
#         self.__private.variable = "This is a private variable"
#         # self.public_variable = "This is a public variable"
#
#         def __private_method(self):
#             print("This is a private method")
#
# my_Class = MyClass()
# print(my_Class.privte_variable)
# my_Class._private_method()

class MyClass:
    def __init__(self):
        self._protected_variable = "Hello World"

    def _protected_method(self):
        print("Protected method")

my_class = MyClass()

print(my_class._protected_method())

my_class._protected_method()
