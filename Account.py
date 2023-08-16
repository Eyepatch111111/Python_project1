print("*****Welcome*****")


class BankAccount:
    def __init__(self, account_holder_name, balance):
        if balance >= 0:
            self._account_holder_name = account_holder_name
            self._balance = balance
            print("Hey", self._account_holder_name, "your account created with balance:", self._balance)
        else:
            print("invalid")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Amount deposited successfully!! Available balance is", self.check_balance())
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Sorry!! Insufficient balance. You have only", self.check_balance(), "amount.")
        else:
            self._balance -= amount
            print(amount, "Withdrawal successful !! Available balance is", self.check_balance())

    def check_balance(self):
        return self._balance

    def transfer(self, amount, account):
        if amount > self._balance:
            print("Sorry!! Insufficient balance. You have only", self.check_balance(), "amount.")
        else:
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer successful!! Available balance is", self.check_balance())
