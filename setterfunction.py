"""import faker module to take random  data """
from faker import Faker
class Employee:
    """create  a class named as employee"""
    def __init__(self):
        self._employee_id = None
        self._name = None
        self._email = None
        self._business_unit = None
        self._salary = None
        self.fake = Faker()
    @property
    def employee_id(self):
        """Method to return employee_id"""
        return self._employee_id
    @employee_id.setter
    def employee_id(self, value):
        """Method to assign value of employee id"""
        self._employee_id = value
    @property
    def name(self):
        """return employee  name"""
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def email(self):
        """return employee email"""
        return self._email
    @email.setter
    def email(self, value):
        self._email = value
    @property
    def business_unit(self):
        """return  employee business unit"""
        return self._business_unit
    @business_unit.setter
    def business_unit(self, value):
        self._business_unit = value
    @property
    def salary(self):
        """return employee salary"""
        return self._salary
    @salary.setter
    def salary(self, value):
        self._salary = value
    def set_default_values(self):
        """this is set default value method to generate random  details of the employee"""
        self._employee_id = self.fake.unique.random_number(digits=5)
        self._name = self.fake.name()
        self._email = self.fake.email()
        self._business_unit = self.fake.company()
        self._salary = self.fake.random_int(min=30000, max=180000)
# Example usage
employee = Employee()
employee.set_default_values()
print(f"Employee ID: {employee.employee_id}, Name: {employee.name}",
      f"Email: {employee.email}, Business Unit: {employee.business_unit}",
      f"Salary: {employee.salary}")
