import tkinter as tk
from tkinter import ttk, messagebox
from model.customer import Customer
from controller.customer_controller import CustomerController

class CustomerForm:
    def __init__(self, parent):
        self.controller = CustomerController()
        self.window = tk.Toplevel(parent)
        self.window.title("Customer Management")
        self.window.geometry("1000x560")
        left = tk.Frame(self.window); left.pack(side="left", padx=18, pady=15)
        self.entries = {}
        fields = [("customer_id", "Customer ID"), ("name", "Name"),
                  ("address", "Address"), ("date_of_birthday", "Birthday (YYYY-MM-DD)"),
                  ("password", "Password")]
        for key, label in fields:
            tk.Label(left, text=label).pack(anchor="w")
            entry = tk.Entry(left, width=32, show="*" if key == "password" else "")
            entry.pack(pady=4)
            self.entries[key] = entry
        buttons = [("Add Customer", self.add), ("Edit Customer", self.update),
                   ("Delete Customer", self.delete), ("Search", self.search),
                   ("Show All", self.load_table), ("Clear", self.clear)]
        for label, command in buttons:
            tk.Button(left, text=label, width=25, command=command).pack(pady=4)
        right = tk.Frame(self.window); right.pack(side="right", padx=15, pady=15)
        cols = ("id", "name", "address", "birthday")
        self.table = ttk.Treeview(right, columns=cols, show="headings", height=20)
        for col, title in zip(cols, ("Customer ID", "Name", "Address", "Birthday")):
            self.table.heading(col, text=title)
        self.table.pack()
        self.table.bind("<<TreeviewSelect>>", self.select_item)
        self.load_table()

    def values(self):
        return {key: entry.get().strip() for key, entry in self.entries.items()}

    def load_table(self, data=None):
        for row in self.table.get_children(): self.table.delete(row)
        for c in (self.controller.get_all() if data is None else data):
            self.table.insert("", tk.END, values=(c.customer_id, c.name, c.address, c.date_of_birthday))

    def add(self):
        try:
            v = self.values()
            self.controller.add(Customer(v["customer_id"], v["name"], v["address"], v["date_of_birthday"], v["password"]))
            self.load_table(); self.clear()
            messagebox.showinfo("Success", "Customer added")
        except Exception as e: messagebox.showerror("Error", str(e))

    def update(self):
        try:
            v = self.values()
            self.controller.update(Customer(v["customer_id"], v["name"], v["address"], v["date_of_birthday"], v["password"]))
            self.load_table(); self.clear()
            messagebox.showinfo("Success", "Customer updated")
        except Exception as e: messagebox.showerror("Error", str(e))

    def delete(self):
        try:
            customer_id = self.entries["customer_id"].get().strip()
            if not customer_id: raise ValueError("Enter customer ID")
            self.controller.delete(customer_id); self.load_table(); self.clear()
        except Exception as e: messagebox.showerror("Error", str(e))

    def search(self):
        self.load_table(self.controller.search(self.entries["name"].get().strip()))

    def clear(self):
        for entry in self.entries.values(): entry.delete(0, tk.END)

    def select_item(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, "values")
        if values:
            self.clear()
            for key, value in zip(("customer_id", "name", "address", "date_of_birthday"), values):
                self.entries[key].insert(0, value)
