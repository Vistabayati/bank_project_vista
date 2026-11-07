import tkinter as tk
from tkinter import ttk, messagebox
from controller.transaction_controller import TransactionController
from controller.account_controller import AccountController
from controller.customer_controller import CustomerController

class TransactionForm:
    def __init__(self, parent):
        self.controller = TransactionController()
        self.accounts = AccountController()
        self.customers = CustomerController()
        self.window = tk.Toplevel(parent)
        self.window.title("Transactions")
        self.window.geometry("1000x550")
        left = tk.Frame(self.window); left.pack(side="left", padx=20, pady=20)
        tk.Label(left, text="Customer ID").pack(anchor="w")
        self.customer_entry = tk.Entry(left, width=30); self.customer_entry.pack(pady=5)
        tk.Label(left, text="Customer Password").pack(anchor="w")
        self.password_entry = tk.Entry(left, width=30, show="*"); self.password_entry.pack(pady=5)
        tk.Label(left, text="Account Number").pack(anchor="w")
        self.account_entry = tk.Entry(left, width=30); self.account_entry.pack(pady=5)
        tk.Label(left, text="Card PIN (CardAccount only)").pack(anchor="w")
        self.pin_entry = tk.Entry(left, width=30, show="*"); self.pin_entry.pack(pady=5)
        tk.Label(left, text="Amount").pack(anchor="w")
        self.amount_entry = tk.Entry(left, width=30); self.amount_entry.pack(pady=5)
        for label, command in [("Deposit", lambda: self.make("deposit")),
                               ("Withdraw", lambda: self.make("withdraw")),
                               ("Show Transactions", self.load_table),
                               ("Clear", self.clear)]:
            tk.Button(left, text=label, width=25, command=command).pack(pady=6)
        right = tk.Frame(self.window); right.pack(side="right", padx=15, pady=15)
        cols = ("account", "payment", "received", "date", "time")
        self.table = ttk.Treeview(right, columns=cols, show="headings", height=20)
        for col, title in zip(cols, ("Account", "Payment / Withdraw", "Received / Deposit", "Date", "Time")):
            self.table.heading(col, text=title)
        self.table.pack()
        self.load_table()

    def make(self, kind):
        try:
            customer_id = self.customer_entry.get().strip()
            account_number = self.account_entry.get().strip()
            customer = next((c for c in self.customers.get_all() if c.customer_id == customer_id), None)
            if customer is None or not customer.verifyPassword(self.password_entry.get()):
                raise ValueError("Customer ID or password is incorrect")
            account = self.accounts.get_by_number(account_number)
            if account.customer_id != customer_id:
                raise ValueError("This account does not belong to the customer")
            if getattr(account, "account_type", "") == "CardAccount" and not account.verifypin(self.pin_entry.get()):
                raise ValueError("Card PIN is incorrect")
            self.controller.make_transaction(account_number, kind, self.amount_entry.get().strip())
            self.load_table()
            messagebox.showinfo("Success", "Transaction completed")
        except Exception as e: messagebox.showerror("Error", str(e))

    def load_table(self):
        for row in self.table.get_children(): self.table.delete(row)
        number = self.account_entry.get().strip()
        data = self.controller.get_for_account(number) if number else self.controller.get_all()
        for item in data:
            self.table.insert("", tk.END, values=(item["account_number"], item["payment_amount"],
                item["received_amount"], item["date"], item["time"]))

    def clear(self):
        for e in (self.customer_entry, self.password_entry, self.account_entry, self.pin_entry, self.amount_entry):
            e.delete(0, tk.END)
