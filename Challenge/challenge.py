class DigitalSchool:
    def __init__(self, name, city, region, programs):
        self.__name = name
        self.__city = city
        self.__region = region
        self.__programs = programs

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        self.__city = new_city

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, new_region):
        self.__region = new_region

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, new_programs):
        self.__programs = new_programs

    def show_school_info(self):
        return {
            "Digital School": self.__name,
            "Located in": f"{self.__city}, {self.__region}",
            "Programs Offered": self.__programs
        }

    def organize_hackathon(self):
        raise NotImplementedError("Subclasses must implement this method.")


class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, region, programs, student_count):
        super().__init__(name, city, region, programs)
        self.__student_count = student_count

    @property
    def student_count(self):
        return self.__student_count

    def student_count(self, new_count):
        self.__student_count = new_count

    def SCF(self):
        print(" Welcome to DS_Prishtina's Spring Code Fest 2025!")
        print("   Students from all around Kosovo collaborate, compete, and create amazing projects!")
















