class Account:

    def __init__(self, privateKey, publicKey, address):
        self.private = privateKey
        self.public = publicKey
        self.address = address

    def get_address(self):
        return self.address

