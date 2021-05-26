from Business import Business
from BusinessAccount import BusinessAccount
from CheckingAccount import CheckingAccount
from Person import Person
from SavingsAccount import SavingAccount
from TrustAccount import TrustAccount

if __name__ == '__main__':

    # Create Owners
    B1 = Business('Franciscan University', '1235 University BLVD', 'College')
    P1 = Person('Amy', '125 Buick DR', 21)
    P2 = Person('Timothy', ' 421 Organ Trail', 20)
    P3 = Person('Sam', '3145 Adjacent Blvd', 15)
    P4 = Person('Anna', 'Back Country St', 22)

    # Create Accounts with Owners
    SA = SavingAccount(121, 200.00, 20, 3, 5, 20.0, P1)
    TA = TrustAccount(513, 9000000.00, P2, 1.0, 20, 2)
    CA = CheckingAccount(232, 54365.50, P3, 2, 2.0, 5.0)
    TA2 = TrustAccount(512, 9000000.00, P4, 1.0, 20, 5.0)
    BA = BusinessAccount(214, 902134.04, 200.00, 30, 20.0, B1)

# Abstract Array of all Accounts
    AbAc = [SA, TA, CA, TA2, BA]

    # Loop tests all shared functions
    for i in AbAc:
        print('----------------------------------------------')
        print(i.owner.__str__())
        print(i.__str__())
        print(i.balance)
        i.deposit(20)
        print('Just deposited $20 minus fees (if applicable)')
        print(i.balance)
        i.withdraw(15)
        print("Just withdrew from accounts (if Applicable)")

        # Tests unique function within loop
        if i == SA:
            print('The Amount with interest after')
            print(i.calc_interest())
            print(i.balance)
            continue
        print('----------------------------------------------')




