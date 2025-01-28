from functools import reduce

class Employee:
    def __init__(self, employee_id, name, salary, city):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary
        self.__city = city

    def __str__(self):
        return f"ID: {self.__employee_id}, Name: {self.__name}, Salary: {self.__salary}, City: {self.__city}"

    def get_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def __add__(self, other):
        return self.__salary + other.__salary


class Manager(Employee):
    def __init__(self, employee_id, name, salary, city, department):
        super().__init__(employee_id, name, salary, city)
        self.__department = department

    def __str__(self):
        return super().__str__() + f", Department: {self.__department}"


class ManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        for emp in self.employees:
            print(emp)

    def search_employees(self, key, value):
        if key == "name":
            result = filter(lambda emp: emp.get_name().lower() == value.lower(), self.employees)
        elif key == "city":
            result = filter(lambda emp: emp.get_city().lower() == value.lower(), self.employees)
        for emp in result:
            print(emp)

    def edit_employee(self, employee_id, field, value):
        for emp in self.employees:
            if emp.get_id() == employee_id:
                if field == "name":
                    emp.set_name(value)
                elif field == "salary":
                    emp.set_salary(float(value))
                elif field == "city":
                    emp.set_city(value)

    def delete_employee(self, employee_id):
        self.employees = list(filter(lambda emp: emp.get_id() != employee_id, self.employees))

    def employee_names_uppercase(self):
        names = list(map(lambda emp: emp.get_name().upper(), self.employees))
        print(names)

    def filter_high_salary(self, threshold):
        result = filter(lambda emp: emp.get_salary() > threshold, self.employees)
        for emp in result:
            print(emp)

    def total_salary_expenditure(self):
        total = reduce(lambda acc, emp: acc + emp.get_salary(), self.employees, 0)
        print(f"Total Salary Expenditure: {total}")


system = ManagementSystem()
system.add_employee(Employee(101, "Sonu Kumar", 300000, "Delhi"))
system.add_employee(Employee(102, "Monu Sharma", 250000, "Mumbai"))
system.add_employee(Employee(103, "Tonu Pande", 400000, "Pune"))
system.add_employee(Manager(104, "Raju Yadav", 350000, "Bangalore", "IT"))
system.add_employee(Employee(105, "Soni Bhave", 280000, "Hyderabad"))

system.view_employees()
system.employee_names_uppercase()
system.search_employees("city", "Bangalore")
system.edit_employee(103, "salary", 200000)
system.delete_employee(103)
system.view_employees()
system.filter_high_salary(300000)
system.total_salary_expenditure()
