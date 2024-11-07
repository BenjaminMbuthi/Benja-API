# Define the Employee class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} (ID: {self.employee_id}) to {self.salary}")

# Define the Department class
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee {employee.name} (ID: {employee.employee_id}) to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for the {self.department_name} department: {total_salary}")
        return total_salary

    def display_all_employees(self):
        print(f"\nEmployees in {self.department_name} Department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")

# Initialize a department
department = Department("Engineering")

# Interactive flow for managing employees
def department_flow():
    while True:
        action = input("\nEnter 'add employee' to add an employee, 'update salary' to update an employee's salary, 'display' to view all employees, 'total' to view total salary expenditure, or 'exit' to quit: ").strip().lower()
        if action == "add employee":
            name = input("Enter employee's name: ").strip()
            employee_id = input("Enter employee's ID: ").strip()
            try:
                salary = float(input("Enter employee's salary: ").strip())
                employee = Employee(name, employee_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid salary. Please enter a numeric value.")
        elif action == "update salary":
            employee_id = input("Enter employee's ID to update salary: ").strip()
            try:
                new_salary = float(input("Enter the new salary: ").strip())
                employee = next((e for e in department.employees if e.employee_id == employee_id), None)
                if employee:
                    employee.update_salary(new_salary)
                else:
                    print(f"No employee found with ID {employee_id}.")
            except ValueError:
                print("Invalid salary. Please enter a numeric value.")
        elif action == "display":
            department.display_all_employees()
        elif action == "total":
            department.calculate_total_salary_expenditure()
        elif action == "exit":
            print("Exiting the department management system.")
            break
        else:
            print("Invalid action. Please try again.")

# Run the interactive flow
department_flow()
