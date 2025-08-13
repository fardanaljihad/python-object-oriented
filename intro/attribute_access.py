# Reading and Modifying Data in Classes

"""
There are two common approaches to controlling how data is accessed and modified: 
a traditional "Java"-style and the more modern "Python" (and C#) style.
"""

# 1. The traditional way: make the data private and use getters and setters:
from datetime import datetime


class User:
    def __init__(self, username, email, password, isAdmin=False):
        self.username = username
        self._email = email
        self.__password = password
        self.isAdmin = isAdmin

    def get_email(self):
        # Advantage of getter: if we need to make changes to way data is accessed, we can do it just here -- not everywhere we are accessing email
        if self.isAdmin:
            print(f"Email accessed at {datetime.now()}")
            return self._email
        return None  # Explicitly returns None to indicate no access

    def set_email(self, newEmail):
        if "@" in newEmail:
            self._email = newEmail

user1 = User("amonra", "amonra@example.com", "pwd123", True)
print(user1._email)  # NAUGHTY!! As responsible Python devs, we are expected to do this:
print(user1.get_email())  # Controlled access

user1.set_email("amonra@outlook.com")
print(user1.get_email())

print(user1.__password)  # Cannot be accessed

"""
Access Modifiers in Python
In contrast to languages such as Java or C++, which implement strict access control mechanisms (e.g., private or protected), 
Python adopts a more flexible and convention-based approach. In Python:

A single underscore (_) preceding an attribute (e.g., _attribute) serves as a convention indicating that the attribute 
is intended for internal use within a class or module. This convention suggests that it's not part of the public API, 
and external code should be avoided access it directly.

Nevertheless, Python does not enforce this restriction programmatically. These attributes or methods remain accessible from 
outside the class. However, the notation conveys to developers that they are intended to be "protected"
or "internal".

A double underscore (__) serves as a convention similar to a single underscore, but it additionally 
activates Python's name mangling mechanism, which prevents the attribute from being accessed from 
outside the class. The notation conveys to developers that thay are intended to be "private"

The “Consenting Adults” Philosophy
Guido van Rossum's "consenting adults" philosophy highlights Python's emphasis on developer responsibility rather than strict rules. 
This philosophy suggests that:

Developers are trusted to respect the convention of not accessing underscore-prefixed attributes or methods.
Access is not prevented, as Python assumes that developers will act responsibly and won't misuse or 
access "protected" members unless absolutely necessary.
"""
