from BaseAccount import BaseAccount
from Business import Business


class BusinessAccount(BaseAccount, Business):
    def __init__(self, account_number: int, balance: float, withdrawal: float,
                 deposit_amount: float, transaction_fee: float, owner: Business):
        super().__init__(account_number, balance, withdrawal, deposit_amount)
        self.owner = owner
        self.transaction_fee = transaction_fee

    def deposit(self, transaction):
        if self.deposit_amount < 0 or self.deposit_amount == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance += self.deposit_amount - self.transaction_fee

    def withdraw(self, transaction):
        self.withdrawal = transaction
        if self.withdrawal < 0 or self.withdrawal == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance -= (self.withdrawal + self.transaction_fee)

    def __str__(self):
        message = 'The Account Type is Business \n'.format(self=self)
        "Your Account Number is {self.accountNum}\n".format(self=self)
        'The Transaction Fee is set to {self.transaction_fee} \n'.format(self=self)
        return message
