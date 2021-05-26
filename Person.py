class Person(object):
    def __init__(self, name: str, address: str, age: int):
        self.name = name
        self.address = address
        self.age = age

    def get_age(self):
        return self.age

    def get_owner(self):
        return self.name

    def __str__(self):
        message = 'The Owner of the account is {self.name} \n'.format(self=self)
        'Your address is {self.address} \n'.format(self=self)
        'Your age is {self.age}'.format(self=self)
        return message

