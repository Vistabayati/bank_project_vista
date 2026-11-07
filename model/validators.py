import re
from datetime import datetime

def name_validator(value):
    return bool(value and len(value.strip()) >= 2)

def account_number_validator(value):
    return bool(re.fullmatch(r"\d{6,20}", str(value)))

def card_number_validator(value):
    return bool(re.fullmatch(r"\d{16}", str(value)))

def pin_validator(value):
    return bool(re.fullmatch(r"\d{4}", str(value)))

def amount_validator(value):
    try:
        return float(value) > 0
    except (TypeError, ValueError):
        return False

def date_validator(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (TypeError, ValueError):
        return False
