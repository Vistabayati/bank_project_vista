import sys
import os
sys.path.append(os.path.abspath(os.path.join
(os.path.dirname(__file__), '..')))
from model.account import Account

a1 = Account(
    "123456789",
    500000,
    "1001",
)

print(a1.number)
print(a1.balance)
print(a1.customer_id)
