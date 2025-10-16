from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than zero.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than zero.")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"\n Name: {self.name}")
        print(f"   Age: {self.age}")
        print(f"   Weight: {self.weight} kg")
        print(f"   Height: {self.height} m")
        print(f"   BMI: {bmi:.2f}")
        print(f"   Category: {category}")


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"



class Child(Person):
    def calculate_bmi(self):
        # Adjusted BMI formula for children
        return (self.weight / (self.height ** 2)) * 0.9

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"



class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        while True:
            print("\n---  Enter Person Information ---")
            name = input("Name: ")
            age = int(input("Age: "))
            weight = float(input("Weight (kg): "))
            height = float(input("Height (m): "))

            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            self.add_person(person)

            cont = input("Add another person? (y/n): ").lower()
            if cont != 'y':
                break

    def print_results(self):
        print("\n====== BMI Results ======")
        for person in self.people:
            person.print_info()

    def run(self):
        print(" Welcome to the BMI Calculator App (OOP Edition)")
        self.collect_user_data()
        self.print_results()
        print("\n Thank you for using the program!")

if __name__ == "__main__":
    app = BMIApp()
    app.run()


