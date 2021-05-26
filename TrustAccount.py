# Trust Acc inherits Base Acc and receives Person in owner Parameter
from CheckingAccount import CheckingAccount
from Person import Person


class TrustAccount(CheckingAccount):
    def __init__(self,  account_number: int, balance: float, owner: Person, check_fee: float,
                 withdrawal: float, deposit_amount: float):
        super().__init__(account_number, balance, owner, check_fee, withdrawal, deposit_amount)
        self.owner = owner

# If account owner is under 21 they can't withdraw
    def withdraw(self, transaction):
        self.withdrawal = transaction
        if self.owner.get_age() < 21:
            print("Your to young to make a withdraw")

        elif transaction < 0 or transaction == 0:
            print("Hey don't do that you pleabian!!")

        else:
            self.balance -= (transaction + self.check_fee)

    def __str__(self):
        message = 'This is a Trust Account \n'
        "Your Account Number is {self.accountNum}\n".format(self=self)
        'The Check fee is set for ${self.check_fee} \n'.format(self=self)
        return message

