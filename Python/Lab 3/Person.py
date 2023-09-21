class Person:
    def __init__(self, full_name, money = 1000):
        self.full_name = full_name
        self.money = money

    def sleep(self, hours):
        if (hours == 7):
            self.sleep_mode = "happy"
        elif (hours < 7):
           self.sleep_mode = "tired"
        else: 
            self.sleep_mode = "lazy"

    def eat(self, meals):
        if (meals == 3):
            self.health_rate = 100
        elif (meals == 2):
           self.health_rate = 75
        elif (meals == 1): 
            self.health_rate = 50

    def buy(self, items):
        while True:
            if(self.money - (items*10)<0):
                print("You don't have enough money, Enter another number")
            else:
                self.money -= (items*10)
                break


class Employee(Person): 
    def __init__(self, id, email, salary, is_manager, full_name, money= 1000):
        super().__init__(full_name, money= 1000)
        self.id = id
        self.email = email
        self.salary = salary
        self.is_manager = is_manager
        self.emp={
            'id': id,
            "name": full_name,
            "salary": salary,
            "is_manager": is_manager
        }

    def work(self, hours):
        if (hours == 7):
            self.work_mode = "happy"
        elif (hours < 7):
           self.work_mode = "tired"
        else: 
            self.work_mode = "lazy"

   
    def send_Email(self, to, subject, body, receiver_name):
        email_file = open("emails.txt","a")
        email_file.write("------------------------------------------------------------------------\n\n")
        email_file.write("From "+self. email)
        email_file.write("\nTo "+to)
        email_file.write("\nSubject  "+subject)
        email_file.write("\n"+"Dear "+receiver_name+",\n"+body+"\n\n")
        email_file.close()
