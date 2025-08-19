# Inheritance

# Base class representing a generic employee
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def work(self):
        print(f"{self.name} is working.")

# Subclass representing a Manager, inheriting from Employee
class Manager(Employee):
    def __init__(self, employee_id, name, team_size):
        super().__init__(employee_id, name)
        self.team_size = team_size

# Subclass representing a Developer, inheriting from Employee
class Developer(Employee):
    def __init__(self, employee_id, name, programming_language):
        super().__init__(employee_id, name)
        self.programming_language = programming_language

# Example usage
manager = Manager("M001", "Alice", 10)
developer = Developer("D123", "Bob", "Python")

print(manager.__dict__)
manager.work()

print(developer.__dict__)
developer.work()

