from BaseAccount import BaseAccount
from Person import Person


# Checking Acc inherits Base Acc and receives Person
class CheckingAccount(BaseAccount, Person):
    def __init__(self, account_number: int, balance: float, owner: Person,
                 check_fee: float, withdrawal: float, deposit_amount: float):
        super().__init__(account_number, balance, withdrawal, deposit_amount)
        self.owner = owner
        self.check_fee = check_fee

    def deposit(self, transaction):
        self.deposit_amount = transaction
        if transaction < 0 or transaction == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance += self.deposit_amount - self.check_fee

    def withdraw(self, transaction):
        self.withdrawal = transaction
        if transaction < 0 or transaction == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance -= (transaction + self.check_fee)

    def __str__(self):
        message = 'This is Checking Account \n'
        "Your Account Number is {self.accountNum}\n".format(self=self)
        'Your check fee is set for ${self.check_fee} \n'.format(self=self)
        return message
