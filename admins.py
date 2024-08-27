from user import User
from abc import ABC, abstractmethod
class Admin:
    def __init__(self,type,position,level, base_salary):
        super().__init__(type)
        self.set_position(position)
        self.set_level(level)
        self.set_base_salary(base_salary)
    def set_position(self, position):
        if isinstance(position, str):
            self.__position = position
        else:
            raise ValueError("Wrong data type, it should contain letters!!!")

    def set_level(self,level):
        self.__level = level

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def get_position(self):
        return self.__position

    def get_level(self):
        return self.__level

    def get_base_salary(self):
        return self.__position

    def general_report(self):
        pass
    @abstractmethod
    def can_manage(self):
        pass

    @abstractmethod
    def general_reports(self):
        pass

    @abstractmethod
    def can_access(self):
        pass