import tkinter as tk
from tkinter import ttk, messagebox
from model.checking_account import CheckingAccount
from model.saving_account import SavingAccount
from model.card_account import CardAccount
from controller.account_controller import AccountController
from controller.customer_controller import CustomerController

class AccountForm:
    def __init__(self, parent):
        self.controller = AccountController()
        self.customers = CustomerController()
        self.window = tk.Toplevel(parent)
        self.window.title("Account Management")
        self.window.geometry("1050x560")
        left = tk.Frame(self.window); left.pack(side="left", padx=18, pady=15)
        self.entries = {}
        fields = [("number", "Account Number"), ("customer_id", "Customer ID"),
                  ("balance", "Initial Balance"), ("card_number", "Card Number (CardAccount only)"),
                  ("pin", "PIN (CardAccount only)"), ("expire_date", "Expire Date")]
        for key, label in fields:
            tk.Label(left, text=label).pack(anchor="w")
            e = tk.Entry(left, width=32, show="*" if key == "pin" else "")
            e.pack(pady=3); self.entries[key] = e
        tk.Label(left, text="Account Type").pack(anchor="w")
        self.type_var = tk.StringVar(value="CheckingAccount")
        ttk.Combobox(left, textvariable=self.type_var,
                     values=("CheckingAccount", "SavingAccount", "CardAccount"),
                     state="readonly", width=29).pack(pady=4)
        for label, command in [("Add Account", self.add), ("Delete Account", self.delete),
                               ("Search", self.search), ("Show All", self.load_table),
                               ("Clear", self.clear)]:
            tk.Button(left, text=label, width=25, command=command).pack(pady=4)
        right = tk.Frame(self.window); right.pack(side="right", padx=15, pady=15)
        cols = ("number", "customer", "type", "balance", "card")
        self.table = ttk.Treeview(right, columns=cols, show="headings", height=20)
        for col, title in zip(cols, ("Account Number", "Customer ID", "Type", "Balance", "Card Number")):
            self.table.heading(col, text=title)
        self.table.pack(); self.table.bind("<<TreeviewSelect>>", self.select_item)
        self.load_table()

    def make_account(self):
        v = {k: e.get().strip() for k, e in self.entries.items()}
        if not any(c.customer_id == v["customer_id"] for c in self.customers.get_all()):
            raise ValueError("Customer ID does not exist")
        kind = self.type_var.get()
        if kind == "CheckingAccount": return CheckingAccount(v["number"], v["balance"], v["customer_id"])
        if kind == "SavingAccount": return SavingAccount(v["number"], v["balance"], v["customer_id"])
        return CardAccount(v["number"], v["balance"], v["customer_id"], v["card_number"], v["pin"], v["expire_date"])

    def add(self):
        try:
            self.controller.add(self.make_account()); self.load_table(); self.clear()
            messagebox.showinfo("Success", "Account added")
        except Exception as e: messagebox.showerror("Error", str(e))

    def delete(self):
        try:
            number = self.entries["number"].get().strip()
            if not number: raise ValueError("Enter account number")
            self.controller.delete(number); self.load_table(); self.clear()
        except Exception as e: messagebox.showerror("Error", str(e))

    def search(self):
        self.load_table(self.controller.search(self.entries["number"].get().strip()))

    def load_table(self, data=None):
        for row in self.table.get_children(): self.table.delete(row)
        for a in (self.controller.get_all() if data is None else data):
            self.table.insert("", tk.END, values=(a.number, a.customer_id,
                getattr(a, "account_type", "Account"), str(a.balance),
                getattr(a, "card_number", "-")))

    def clear(self):
        for e in self.entries.values(): e.delete(0, tk.END)

    def select_item(self, event):
        values = self.table.item(self.table.focus(), "values")
        if values:
            self.clear()
            for key, value in zip(("number", "customer_id", "balance", "card_number"), (values[0], values[1], values[3], values[4])):
                self.entries[key].insert(0, value)
            self.type_var.set(values[2])
