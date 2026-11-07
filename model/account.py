from decimal import Decimal, InvalidOperation
from model.validators import account_number_validator

class Account:
    def __init__(self, number, balance, customer_id):
        self.number = str(number).strip()
        self.customer_id = str(customer_id).strip()
        self.balance = balance

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not account_number_validator(value):
            raise ValueError("شماره حساب باید بین ۶ تا ۲۰ رقم باشد")
        self.__number = str(value)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        try:
            amount = Decimal(str(value))
        except InvalidOperation:
            raise ValueError("موجودی نامعتبر است")
        if amount < 0:
            raise ValueError("موجودی نمی‌تواند منفی باشد")
        self.__balance = amount

    def deposit(self, amount):
        amount = Decimal(str(amount))
        if amount <= 0:
            raise ValueError("مبلغ باید بیشتر از صفر باشد")
        self.balance = self.balance + amount
        return amount

    def withdraw(self, amount):
        amount = Decimal(str(amount))
        if amount <= 0:
            raise ValueError("مبلغ باید بیشتر از صفر باشد")
        if amount > self.balance:
            raise ValueError("موجودی کافی نیست")
        self.balance = self.balance - amount
        return amount

    def __str__(self):
        return f"{self.number} | {self.balance}"
