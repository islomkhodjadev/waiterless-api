from random import randint


class OTP:

    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def send(self):
        print(f"{self.phoneNumber}\ncode: {randint(1000, 9999)}")

    @classmethod
    def verify(cls, phoneNumber, code): ...
