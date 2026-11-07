import sys
import os
sys.path.append(os.path.abspath(os.path.join
(os.path.dirname(__file__), '..')))
from model.card_account import CardAccount

card1 = CardAccount(
    "1122334455",
    1000000,
    "1001",
    "1234567812345678",
    "1234",
    "2028-05",
)

print(card1.number)
print(card1.balance)
print(card1.customer_id)
print(card1.card_number)
print(card1.pin)
print(card1.expire_date)
print(card1.account_type)
