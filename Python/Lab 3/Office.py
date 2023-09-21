from Person import *
import json
class Office():
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        for emp_data in self.employees:
            print(emp_data)

    def get_employee(self, empId, is_manager):
        for employee in self.employees:
            if(employee["id"] == empId):
                if(is_manager):
                    print(employee)
                else:
                    print("id:",employee["id"])
                    print("name:",employee["name"])
                    print("is_manager:",employee["is_manager"])

    def fire(self, empId):
        for emp_data in self.employees:
            if (emp_data["id"] == empId):
                self.employees.remove(emp_data)

    def hire(self):
        id = int(input("Enter id: "))
        full_name = input("Enter full name: ")
        email = input("Enter email: ")
        salary = int(input("Enter salary: "))
        is_manager = input("Are they a manager? (y/n): ")
        if(is_manager == "y"):
            is_manager = True
        else:
            is_manager = False
        employee = Employee(id, email, salary,is_manager, full_name)
        self.employees.append(employee.emp)