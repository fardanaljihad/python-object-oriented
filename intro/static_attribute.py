# A static attribute (or class attribute) is an attribute that belongs to the class itself, 
# not to any specific instance of the class. In real-world applications, 
# static attributes are useful for storing values that should be consistent across all objects, 
# such as an interest rate in a banking system.

class User:
    # Static attribute (common) to count all users
    user_count = 0  # Advantage: it is associated directly with the class

    def __init__(self, username, password):
        self.username = username  # Instance attribute (unique)
        self.password = password  # Instance attribute
        User.user_count += 1

    def display_name(self):
        print(f"Username: {self.username}, Password: {self.password}")


user1 = User("amonra", "pwd123")
user2 = User("aurora", "pwd321")

# Accessing static attribute
print(User.user_count)
print(user1.user_count)
print(user2.user_count)

# A static attribute is useful when the data is common to all instances of a class. 
# Instead of duplicating the same value in every object, the attribute is stored 
# once at the class level and shared by all instances. This ensures consistency and reduces memory usage.
