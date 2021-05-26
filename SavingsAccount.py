from BaseAccount import BaseAccount
from Person import Person


# Savings Account inherits Base Account and adds unique functions and receives Person
class SavingAccount(BaseAccount):
    def __init__(self, account_number: int, balance: float, interest_rate: float, years: int,
                 withdrawal: float, deposit_amount: float, owner: Person):
        super().__init__(account_number, balance, withdrawal, deposit_amount)
        self.interestRate = interest_rate
        self.years = years
        self.owner = owner

    def get_interest(self):
        return self.interestRate

    def calc_interest(self):
        self.balance = (self.balance * self.years * self.interestRate) / 100
        return self.balance

    def __str__(self):
        message = 'Account Type: Savings'
        "Account Number: {self.accountNum}\n".format(self=self)
        'Interest Rate: {self.interestRate} \n'.format(self=self)
        'Years set for this account is {self.years} \n'.format(self=self)
        return message
