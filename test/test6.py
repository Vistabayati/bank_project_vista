import sys
import os
sys.path.append(os.path.abspath(os.path.join
(os.path.dirname(__file__), '..')))
from model.transaction import Transaction

tr1 = Transaction(
    20000,
    0,
    "2026-11-06",
    "12:30:00",
)

print(tr1.payment_amount)
print(tr1.received_amount)
print(tr1.date)
print(tr1.time)
