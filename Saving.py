from Account import BankAccount


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        # adding amount with 3% interest
        if amount > 0:
            bonus = amount * 0.03
            super().deposit(amount + bonus)
