"""import faker TO create the random data"""
import json
import random
from faker import Faker
# Initialize Faker to generate fake data
fake = Faker()
# Generate fake employee personal details
employee_details = []
class Employee:
    """EMPLOYEE CLASS TO STORE THE DETAILS OF ALL THE EMPLOYEES"""
    def __init__(self, emp_id, emp_name,
                 emp_email,business_unit,salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.business_unit = business_unit
        self.salary=salary
for _ in range(random.randint(10, 20)):
    empid = fake.random_number(digits=5)
    empname = fake.name()
    empemail = fake.email()
    businessunit = fake.company()
    Salary = fake.random_number(digits=5)
    employee_details.append({
        "EMP ID": empid,
        "EMP NAME": empname,
        "EMP EMAIL": empemail,
        "Business Unit": businessunit,
        "Salary": Salary
    })
# Write data to JSON file
with open("Employee_Personal_Details.json", "w",encoding="utf-8") as json_file:
    json.dump(employee_details, json_file, indent=4)
#"Employee personal details generated and saved in 'Employee_Personal_Details.json'")
# Load data into Employee objects
employees = []
for record in employee_details:
    employee = Employee(record["EMP ID"],
                        record["EMP NAME"], record["EMP EMAIL"],
                          record["Business Unit"], record["Salary"])
    employees.append(employee)
# Example usage
for emp in employees:
    print(f"Employee ID: {emp.emp_id}, Name: {emp.emp_name}",
          f"Email: {emp.emp_email}, Business Unit: {emp.business_unit}",
          f"Salary: {emp.salary}")
