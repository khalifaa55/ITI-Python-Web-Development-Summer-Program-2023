from Functions import *
def MainMenu():
    main_file = "employees.json"
    emp_list = read_from_file(main_file)
    
    while True:
        print("--------------------------------------\n\tWelcome to the office\n")
        position=input("-If you're a manager write 'mngr'\n-If you're a normal employee write'nrml'\n")
        if (position == "mngr"):
            is_manager = True
        elif (position == "nrml"):
            is_manager = False
        else:
            print("Error: incorrect position, try again")
            continue

        id = int(input("Enter your id: "))
        new_user = True
        for emp_data in emp_list:
            if (id == emp_data["id"]):
                new_user = False
        full_name = input("Enter your full name: ")
        email = input("Enter your email: ")
        salary = int(input("Enter your salary: "))
        employee = Employee(id, email, salary,is_manager, full_name)
        if (new_user):
            emp_list.append(employee.emp)
        office_name = input("Enter name of your office: ")
        office = Office(office_name, emp_list)
        break

    while True: 
        print("--------------------------------------\n\tMain Menu\n")
        print("-To hire new employee write 'h'")
        print("-To write email write 'e'")
        print("-To get all employees write 'a'")
        print("-To get an employee write 'g'")
        print("-To fire employee write 'f'")
        print("-To quit write 'q'")
        option = input("\n")
        if(option=="h"):
            AddEmp(office)
        elif(option=="e"):
            Email(employee)
        elif(option=="a"):
            GetAll(office)
        elif(option=="g"):
            GetEmp(is_manager, office)
        elif(option=="f"):
            Fire(office)
        elif(option=="q"):
            print("Thank you for your time")
            write_to_file(main_file, emp_list)
            break
        else:
            print("invalid option, try again")
            continue
MainMenu()