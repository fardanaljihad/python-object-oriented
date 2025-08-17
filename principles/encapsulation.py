# Encapsulation

# The design of this class is problematic because the `balance` attribute can be directly modified 
# and even initialized with invalid values. In real-world banking systems, allowing a negative balance 
# without explicit rules or validation violates essential business logic and data integrity constraints.
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1  # A negative balance should be disallowed.
print(account.balance)


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    # "Getter" property provides controlled access to _balance attr.
    @property
    def balance(self):
        return self._balance
    
    """
    If a setter property is not defined, the attribute `_balance` cannot be directly modified from outside the class. 
    This design enforces encapsulation by preventing invalid assignments and ensuring data integrity. 
    Any modification to `_balance` must occur exclusively through the defined `deposit` and `withdraw` methods, 
    which act as the controlled interface for maintaining valid state transitions.
    """
    # @balance.setter
    # def balance(self, amount):
    #   self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Transaction declined: insufficient balance.")
        self._balance -= amount

account2 = BankAccount()
print(account2.balance)
# account2.balance = -1 # This would give ERROR: Cannot assign to attribute "balance" for class "BankAccount"
account2.deposit(99.9)
print(account2.balance)
account2.withdraw(19.9)
print(account2.balance)
account2.withdraw(100)
