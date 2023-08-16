from Account import BankAccount


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount > self._balance:
            print("Sorry!! Insufficient balance. You have ", self.check_balance(), "amount.")
        else:
            charge = 200
            super().withdraw(amount + charge)
            print("Withdrawal successful!! Available balance is", self.check_balance())
