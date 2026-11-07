from model.validators import name_validator, date_validator

class Customer:
    def __init__(self, customer_id, name, address, date_of_birthday, password):
        self.customer_id = str(customer_id).strip()
        self.name = name
        self.address = address
        self.date_of_birthday = date_of_birthday
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not name_validator(value):
            raise ValueError("نام مشتری معتبر نیست")
        self.__name = value.strip()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not value or len(value.strip()) < 3:
            raise ValueError("آدرس باید حداقل ۳ کاراکتر باشد")
        self.__address = value.strip()

    @property
    def date_of_birthday(self):
        return self.__date_of_birthday

    @date_of_birthday.setter
    def date_of_birthday(self, value):
        if not date_validator(value):
            raise ValueError("تاریخ تولد باید با قالب YYYY-MM-DD باشد")
        self.__date_of_birthday = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not value or len(value) < 4:
            raise ValueError("رمز مشتری باید حداقل ۴ کاراکتر باشد")
        self.__password = value

    def verifyPassword(self, password):
        return self.password == password

    def __str__(self):
        return f"{self.customer_id} | {self.name}"
