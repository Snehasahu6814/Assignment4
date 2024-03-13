"""importing json library to store the details of the employee in the json format """
import json
class Employee:
    """class Employee which stores the details of the Employees"""
    def __init__(self,employee_id,
                 name,email,business_unit,salary):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.business_unit = business_unit
        self.salary = salary
    def to_dict(self):
        """Assigning the details of employee """
        return {
            "EMP ID": self.employee_id,
            "EMP NAME": self.name,
            "EMP EMAIL": self.email,
            "Business Unit": self.business_unit,
            "Salary": self.salary
        }
    @staticmethod
    def to_json_and_write(employees=None, file_name="employees.json"):
        """Converting the employee details into the json format"""
        if employees is None:
            employees = []
        # Convert to JSON
        if isinstance(employees, list):
            data = [emp.to_dict() for emp in employees]
        else:
            data = employees.to_dict()
        # Write to file
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
employee1 = Employee(1,"Julia Rollins","lucashernandez@example.net","Developer",87653)
employee2 = Employee(2,"Gerald Moore","robertroberson@example.com","Tester",98765)
employee3 = Employee(3, "Shane Patterson", "summerkramer@example.org","HR", 95479)
# Writing one employee  details to the file
employee1.to_json_and_write(file_name="employee_details.json")
# Writing a list of employees  details to the file
employees_list = [employee1, employee2, employee3]
Employee.to_json_and_write(employees_list, "employees_detail_list.json")
# Writing all employees details (by default) to file
Employee.to_json_and_write()
