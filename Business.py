class Business(object):
    def __init__(self, name: str, address: str, b_type: str):
        self.name = name
        self.address = address
        self.b_type = b_type

    def get_owner(self):
        return self.name

    def __str__(self):
        message = 'The owner of the account is {self.name} \n'.format(self=self)
        'Your address is {self.address} \n'.format(self=self)
        'Your Business Type is {self.b_type}'.format(self=self)
        return message
