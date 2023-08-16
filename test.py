from Account import BankAccount
from Saving import SavingsAccount
from Currentaccount import CurrentAccount

B1 = BankAccount("ritul", 500)
B2 = BankAccount("Rakesh", 200)
B1.withdraw(200)
B2.deposit(1000)
B2.transfer(500, B1)
print(B1.check_balance())
print(B2.check_balance())

S1 = SavingsAccount("Vivek", 2000)
S1.deposit(500)
print(S1.check_balance())

C1 = CurrentAccount("Vivek", 2000)
C1.deposit(500)
C1.withdraw(100)
C1.transfer(500, S1)

print(S1.check_balance())
print(C1.check_balance())

