class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, accname):
        self.balance = initial_amount
        self.name = accname
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        print(f"\nAccount '{self.name}' Deposited ${amount:.2f}")
        self.get_balance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
            
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw_balance(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            print(f"\nAccount '{self.name}' Withdrawn ${amount:.2f}")
            self.get_balance()
        except BalanceException as erorr:
            print(f"\nWithdraw interrupted: {erorr}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBegining Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw_balance(amount)
            account.deposit(amount)
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as erorr:
            print(f"\nTransfer interrupted. ❌ {erorr}")


class InteresetRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()


class SavingsAccount(InteresetRewardsAccount):
    def __init__(self, initial_amount, accname):
        super().__init__(initial_amount, accname)
        self.fee = 5
    
    def withdraw_balance(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance  - (amount + self.fee)
            print("\nWithdraw completed.")
            self.get_balance()
        except BalanceException as erorr:
            print(f"\nWithdraw interrupted ❌: {erorr}")

