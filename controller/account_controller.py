from utils.file_manager import FileManager

class AccountController:
    file_name = "data/accounts.pkl"

    def get_all(self):
        return FileManager.load(self.file_name)

    def add(self, account):
        data = self.get_all()
        if any(a.number == account.number for a in data):
            raise ValueError("شماره حساب تکراری است")
        if getattr(account, "account_type", "") == "CardAccount":
            if any(getattr(a, "card_number", None) == account.card_number for a in data):
                raise ValueError("شماره کارت تکراری است")
        customer_accounts = [a for a in data if a.customer_id == account.customer_id]
        if len(customer_accounts) >= 2:
            raise ValueError("هر مشتری حداکثر می‌تواند دو حساب داشته باشد")
        data.append(account)
        FileManager.save(self.file_name, data)

    def update(self, new_account):
        data = self.get_all()
        for i, account in enumerate(data):
            if account.number == new_account.number:
                data[i] = new_account
                FileManager.save(self.file_name, data)
                return
        raise ValueError("حساب پیدا نشد")

    def delete(self, number):
        data = [a for a in self.get_all() if a.number != str(number)]
        FileManager.save(self.file_name, data)

    def search(self, text):
        return [a for a in self.get_all() if text in a.number or text in a.customer_id]

    def get_by_number(self, number):
        for account in self.get_all():
            if account.number == str(number):
                return account
        raise ValueError("حساب پیدا نشد")
