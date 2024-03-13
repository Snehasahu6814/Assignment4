"""import faker"""
from faker import Faker
class Employee:
    """create a class Employee"""
    def __init__(self):
        self._employee_id = None
        self._name = None
        self._email = None
        self._business_unit = None
        self._salary = None
        self.fake = Faker()
    def get_employee_id(self):
        """to get the employee id"""
        return self._employee_id
    def get_name(self):
        """to get the employee name"""
        return self._name
    def get_email(self):
        """to get the employee email"""
        return self._email
    def get_business_unit(self):
        """to get the employee business unit"""
        return self._business_unit
    def get_salary(self):
        """to get the employee salary"""
        return self._salary
    def set_default_values(self):
        """set the default value"""
        self._employee_id = self.fake.unique.random_number(digits=4)
        self._name = self.fake.name()
        self._email = self.fake.email()
        self._business_unit = self.fake.company()
        self._salary = self.fake.random_int(min=30000, max=160000)
# Example usage
employee = Employee()
employee.set_default_values()
print(f"EmployeeID: {employee.get_employee_id()}, Name: {employee.get_name()}"
      f", Email: {employee.get_email()}"
      f", Business Unit: {employee.get_business_unit()}, Salary: {employee.get_salary()}")
