# Static method example

class Account:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive")

    # Protected method: intended for use within the class and its subclasses
    def _is_valid_amount(self, amount):
        return amount > 0
    
    # Private method: intended for use only within the class
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")

    # Static method: belongs to the class, not to any specific instance.
    # It is used for functionality that is logically related to the class,
    # but does not require access to instance-level (self) or class-level (cls) data.
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account1 = Account("Amonra", 900)
account1.deposit(600)

print(Account.is_valid_interest_rate(3))
print(Account.is_valid_interest_rate(7))
