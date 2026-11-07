import sys
import os
sys.path.append(os.path.abspath(os.path.join
(os.path.dirname(__file__), '..')))
from model.saving_account import SavingAccount

sa1 = SavingAccount(
    "987654321",
    750000,
    "1001",
)

print(sa1.number)
print(sa1.balance)
print(sa1.customer_id)
print(sa1.account_type)
