import sys
import os
sys.path.append(os.path.abspath(os.path.join
(os.path.dirname(__file__), '..')))
from model.customer import Customer

c1 = Customer(
    "1001",
    "vista bayati",
    "Tehran",
    "2005-04-12",
    "1234",
)

print(c1.customer_id)
print(c1.name)
print(c1.address)
print(c1.date_of_birthday)
print(c1.password)
