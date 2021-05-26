# Base Account will be inherited by all Accounts
class BaseAccount(object):
    def __init__(self, account_number: int, balance: float, withdrawal: float, deposit_amount: float):
        self.accountNum = account_number
        self.balance = balance
        self.withdrawal = withdrawal
        self.deposit_amount = deposit_amount

    def get_acc_number(self):
        return self.accountNum

    def deposit(self, transaction):
        self.deposit_amount = transaction
        if transaction < 0 or transaction == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance += transaction

    def withdraw(self, transaction):
        self.withdrawal = transaction
        if transaction < 0 or transaction == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance -= transaction

    def get_balance(self):
        return self.balance

