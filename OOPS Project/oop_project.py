from bank_accounts import * # To import everything

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)
Dave.withdraw(4000)
Dave.withdraw(10)

Dave.transfer(100000, Sara)
Dave.transfer(100, Sara)

Jim = InterstRewardAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Sara)