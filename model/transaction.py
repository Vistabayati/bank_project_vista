from datetime import datetime
from decimal import Decimal

class Transaction:
    def __init__(self, payment_amount=0, received_amount=0, date=None, time=None):
        self.payment_amount = Decimal(str(payment_amount))
        self.received_amount = Decimal(str(received_amount))
        now = datetime.now()
        self.date = date or now.strftime("%Y-%m-%d")
        self.time = time or now.strftime("%H:%M:%S")
        self._modified = False

    def modifies(self, account):
        if self._modified:
            raise ValueError("این تراکنش قبلاً اعمال شده است")
        if self.payment_amount > 0 and self.received_amount > 0:
            raise ValueError("یک تراکنش نمی‌تواند هم‌زمان واریز و برداشت باشد")
        if self.payment_amount > 0:
            account.withdraw(self.payment_amount)
        elif self.received_amount > 0:
            account.deposit(self.received_amount)
        else:
            raise ValueError("مبلغ تراکنش نامعتبر است")
        self._modified = True
        return account

    def __str__(self):
        kind = "برداشت" if self.payment_amount else "واریز"
        amount = self.payment_amount or self.received_amount
        return f"{kind} | {amount} | {self.date} | {self.time}"
