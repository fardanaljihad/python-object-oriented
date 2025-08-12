# Everything created in Python is an object. For example:

owner = "Basket Case"
balance = 99999999999.9

print(type(owner))     # <class 'str'>
print(type(balance))    # <class 'float'>

# Classes
class Bank:
    def __init__(self, name, code):
        """
        The __init__ method is a special method that runs only once when an object is created (instantiated). 
        Here is an example for setup object data:
        
        bank1 = Bank("World Bank", "WB")
        """
        self.name = name
        self.code = code
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_info(self):
        print(f"{self.name} | {self.code} | Number of Account: {len(self.accounts)}")


class Account:
    def __init__(self, number, owner, bank):
        self.number = number
        self.owner = owner
        self.bank = bank
        bank.add_account(self)

    def __str__(self):
        """
        Special method that returns a human-readable string representation of the object.
        Automatically called when the object is printed or converted to a string using str().
        """
        return f"Account: {self.number} - Owner: {self.owner} ({self.bank.name})"
    
# Objects
bank1 = Bank("World Bank", "WB")
account1 = Account("123456789", "Adit", bank1)
account2 = Account("987654321", "Denis", bank1)

bank1.get_info()
print(account1)
print(account2)
