import bank_account as bq

Saad = bq.BankAccount(2000, "Saad")
Ahmed = bq.BankAccount(1000, "Ahmed")

Saad.get_balance()
Ahmed.get_balance()

Saad.deposit(500)

Ahmed.withdraw_balance(2000)
Ahmed.withdraw_balance(20)

Ahmed.transfer(100, Saad)


Ali = bq.InteresetRewardsAccount(1000, "Ali")
Ali.get_balance()
Ali.deposit(100)

Ali.transfer(100, Ahmed)

Rasheed = bq.SavingsAccount(1000, "Rasheed")

Rasheed.get_balance()

Rasheed.deposit(100)
Rasheed.transfer(1000, Saad)