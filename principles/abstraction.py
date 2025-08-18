# Abstraction

# Reduce complexity by hiding unnecessary details

from abc import ABC, abstractmethod

# Example without abstraction
class BadPaymentService:
    def connect_to_bank(self):
        print("Connecting to bank server...")

    def verify_account(self):
        print("Verifying account...")

    def deduct_balance(self):
        print("Deducting from account...")

    def confirm_transaction(self):
        print("Transaction confirmed.\n")


# The user must know and call each step in the correct order
bad_payment = BadPaymentService()
bad_payment.connect_to_bank()
bad_payment.verify_account()
bad_payment.deduct_balance()
bad_payment.confirm_transaction()


# Example with abstraction
class PaymentService(ABC):
    # Abstract method that enforces subclasses to implement payment logic
    @abstractmethod
    def pay(self):
        pass


class Payment(PaymentService):
    # Internal helper methods (hidden implementation details)
    def _connect_to_bank(self):
        print("Connecting to bank server...")

    def _verify_account(self):
        print("Verifying account...")

    def _deduct_balance(self):
        print("Deducting from account...")

    def _confirm_transaction(self):
        print("Transaction confirmed.")

    # Abstraction: the user only needs to call `pay()`,
    # without worrying about the internal steps
    def pay(self):
        self._connect_to_bank()
        self._verify_account()
        self._deduct_balance()
        self._confirm_transaction()


# The user only calls one method (high-level interface)
payment = Payment()
payment.pay()
