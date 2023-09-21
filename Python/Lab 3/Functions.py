from Office import *

def read_from_file(filename):
    data_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces and newline characters
            if line:
                try:
                    data = json.loads(line)
                    data_list.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON at line: {line}")
                    print(f"Error details: {e}")
    return data_list

def AddEmp(office):
    office.hire()

def Email(employee):
    to = input("Write email of receiver: ")
    subject = input("Write email subject: ")
    body = input("Write body of email: ")
    receiver_name = input("Write receiver's full name: ")
    employee.send_Email(to, subject, body, receiver_name)

def GetAll(office):
    office.get_all_employees()

def GetEmp(is_manager, office):
    id = int(input("Enter id of employee: "))
    office.get_employee(id, is_manager)

def Fire(office):
    id = int(input("Enter id of employee: "))
    office.fire(id)

def write_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for employee_data in data_list:
            json.dump(employee_data, file)
            file.write('\n')