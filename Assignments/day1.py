# Employee Management System

employees = [
    {"employee_id": 101, "name": "Sonu Kumar", "salary": 300000, "city": "Delhi"},
    {"employee_id": 102, "name": "Monu Sharma", "salary": 250000, "city": "Mumbai"},
    {"employee_id": 103, "name": "Tonu Pande", "salary": 400000, "city": "Pune"},
    {"employee_id": 104, "name": "Raju Yadav", "salary": 350000, "city": "Bangalore"},
    {"employee_id": 105, "name": "Soni Bhave", "salary": 280000, "city": "Hyderabad"}
]

# MENU
def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Edit Employee Details")
    print("5. Delete Employee")
    print("6. Exit")

# ADD
def add_employee():
    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    city = input("Enter Employee City: ")
    employees.append({"employee_id": employee_id, "name": name, "salary": salary, "city": city})
    print("Employee added successfully!")

# VIEW
def view_employees():
        print("\nEmployee List:")
        for emp in employees:
            print(f"ID: {emp['employee_id']}, Name: {emp['name']}, Salary: {emp['salary']}, City: {emp['city']}")

# SEARCH
def search_employee():
    criteria = input("Search by (name/city): ").strip().lower()
    value = input(f"Enter {criteria.capitalize()}: ").strip()
    results = [emp for emp in employees if emp[criteria].lower() == value.lower()]
    if results:
        print("\nSearch Results:")
        for emp in results:
            print(f"ID: {emp['employee_id']}, Name: {emp['name']}, Salary: {emp['salary']}, City: {emp['city']}")
    else:
        print("No employees found.")

# EDIT
def edit_employee():
    employee_id = int(input("Enter Employee ID to edit: "))
    for emp in employees:
        if emp["employee_id"] == employee_id:
            print("1. Edit Name\n2. Edit Salary\n3. Edit City")
            choice = int(input("What would you like to edit? "))
            if choice == 1:
                emp["name"] = input("Enter new name: ")
            elif choice == 2:
                emp["salary"] = float(input("Enter new salary: "))
            elif choice == 3:
                emp["city"] = input("Enter new city: ")
            else:
                print("Invalid choice!")
                return
            print("Employee details updated")
            return
    print("Employee not found.")

# DELETE EMPLOYEE
def delete_employee():
    employee_id = int(input("Enter Employee ID to delete: "))
    global employees
    employees = [emp for emp in employees if emp["employee_id"] != employee_id]
    print("Employee deleted successfully!" if len(employees) != len(employees) else "Employee not found.")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            edit_employee()
        elif choice == 5:
            delete_employee()
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()