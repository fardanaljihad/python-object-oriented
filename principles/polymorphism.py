# Polymorphism

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return 0
    
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.salary * 0.20
    
class Developer(Employee):
    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role

    def calculate_bonus(self):
        return self.salary * 0.10
    
class Intern(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return 500.0
    

"""
Problem: Without polymorphism, the logic is centralized in one function.
This creates tight coupling between the function and all employee roles (subclasses).
Every time we add a new employee type or change the bonus rule,
we must modify this function, violating the Open/Closed Principle.
"""
# def bad_calculate_bonus(employee):
#     if isinstance(employee, Manager):
#         return employee.salary * 0.20
#     elif isinstance(employee, Developer):
#         return employee.salary * 0.10
#     elif isinstance(employee, Intern):
#         return 500
#     else:
#         return 0

# Open/Closed Principle: classes should be open for extension but closed for modification.  


# Demonstration of polymorphism
employees = [
    Manager("Alice", 8000, 10),
    Developer("Bob", 6000, "Junior Odoo Developer"),
    Intern("Charlie", 2000)
]

for emp in employees:
    print(f"{emp.name} receives a bonus of ${emp.calculate_bonus()}")
