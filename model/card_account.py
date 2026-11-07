from model.account import Account
from model.validators import card_number_validator, pin_validator

class CardAccount(Account):
    def __init__(self, number, balance, customer_id, card_number, pin, expire_date):
        super().__init__(number, balance, customer_id)
        self.card_number = card_number
        self.pin = pin
        self.expire_date = expire_date
        self.account_type = "CardAccount"

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, value):
        if not card_number_validator(value):
            raise ValueError("شماره کارت باید دقیقاً ۱۶ رقم باشد")
        self.__card_number = str(value)

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if not pin_validator(value):
            raise ValueError("رمز کارت باید دقیقاً ۴ رقم باشد")
        self.__pin = str(value)

    def verifypin(self, pin):
        return self.pin == str(pin)
