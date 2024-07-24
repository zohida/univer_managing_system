from user import User
from abc import ABC, abstractmethod
class Staff(User):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, salary,title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone)
        self.set_occupation(occupation)
        self.set_profile(profile)
        self.set_salary(salary)
        self.set_title(title)
    def set_occupation(self, occupation):
        if occupation.lower() == "part-time" or occupation.lower() == "full-time":
            self.__occupation = occupation
        else:
            raise ValueError("Occupation should be part or full-time")
    def set_profile(self, profile):
        if isinstance(profile, str):
            self.__profile = profile
        else:
            raise ValueError("Invalid Profile name!!!")

    def set_salary(self, salary):
        if isinstance(salary, int):
            self.__salary = salary
        else:
            raise ValueError("The Salary should be integer value")

    def set_title(self, title):
        title_list = []
        with open("title.txt", "r") as f:
            content = f.readlines()
            for line in content:
                words = line.strip().split(",")
                for word in words:
                    title_list.append(word.strip())

        if title.lower() in (word.lower() for word in title_list):
            self.__title = title
        else:
            raise Exception("Invalid title")

    def get_occupation(self):
        return self.__occupation

    def get_profile(self):
        return self.__profile

    def get_salary(self):
        return self.__salary

    def get_title(self):
        return self.__title

    @abstractmethod
    def work(self):
        pass

staff = Staff("staff","John Smith", "AA0000101",
              "johnsmith@gmail.com", "1995/02/12", "male", "English", "998901001010",
              "full-time", "john_smith", 20000, "academic adviser")

print(staff.get_profile())
