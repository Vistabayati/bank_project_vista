from utils.file_manager import FileManager
from model.transaction import Transaction
from controller.account_controller import AccountController

class TransactionController:
    file_name = "data/transactions.pkl"

    def __init__(self):
        self.account_controller = AccountController()

    def get_all(self):
        return FileManager.load(self.file_name)

    def get_for_account(self, account_number):
        return [item for item in self.get_all() if item["account_number"] == str(account_number)]

    def make_transaction(self, account_number, kind, amount):
        account = self.account_controller.get_by_number(account_number)
        transaction = Transaction(
            payment_amount=amount if kind == "withdraw" else 0,
            received_amount=amount if kind == "deposit" else 0
        )
        transaction.modifies(account)
        self.account_controller.update(account)
        data = self.get_all()
        data.append({
            "account_number": str(account_number),
            "payment_amount": str(transaction.payment_amount),
            "received_amount": str(transaction.received_amount),
            "date": transaction.date,
            "time": transaction.time
        })
        FileManager.save(self.file_name, data)
        return transaction
