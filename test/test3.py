import sys
import os
sys.path.append(os.path.abspath(os.path.join
(os.path.dirname(__file__), '..')))
from model.checking_account import CheckingAccount

ca1 = CheckingAccount(
    "123456789",
    500000,
    "1001",
)

print(ca1.number)
print(ca1.balance)
print(ca1.customer_id)
print(ca1.account_type)
