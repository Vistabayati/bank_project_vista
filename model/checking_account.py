from model.account import Account

class CheckingAccount(Account):
    def __init__(self, number, balance, customer_id):
        super().__init__(number, balance, customer_id)
        self.account_type = "CheckingAccount"
