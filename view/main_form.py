import tkinter as tk
from view.customer_form import CustomerForm
from view.account_form import AccountForm
from view.transaction_form import TransactionForm

class MainForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bank Management System")
        self.window.geometry("420x330")
        tk.Label(self.window, text="Bank Management System",
                 font=("Arial", 16, "bold")).pack(pady=25)
        tk.Button(self.window, text="Customers", width=28,
                  command=self.open_customers).pack(pady=8)
        tk.Button(self.window, text="Accounts", width=28,
                  command=self.open_accounts).pack(pady=8)
        tk.Button(self.window, text="Transactions", width=28,
                  command=self.open_transactions).pack(pady=8)
        self.window.mainloop()
    def open_customers(self):
            CustomerForm(self.window)
    def open_accounts(self):
            AccountForm(self.window)
    def open_transactions(self):
            TransactionForm(self.window)
