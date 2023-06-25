class Accountss:
    balance: int
    pin: str
    first_name: str
    last_name: str
    age: int
    phone_number: str
    card_number: str

    def set_Account(self, first_name: str, last_name: str, age: int, phone_Number: str, pin: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_Number
        self.pin = pin

    def deposit(self, amount: int, receive_account):
        if receive_account == self.card_number:
            if amount > 0:
                self.balance += amount

    def check_Balance(self, account_number: str):
        if account_number == self.card_number:
            return self.balance
        else:
            return 0

    def withdraw(self, pin: str, amount: int, acc_num: str):
        self.check_Pin(pin, acc_num)
        if amount > 0:
            if self.balance > amount:
                self.balance = self.balance - amount

    def check_Pin(self, pin: str, acc_num: str):
        if self.card_number == acc_num:
            if pin != self.pin:
                raise AttributeError("Wrong pin")

    def get_Card_number(self):
        return self.card_number

    def set_Account_Number(self, card_number: str):
        self.card_number = card_number

    def create_Account_Number(self, phone_number: str):
        cad = slice(1, 11)
        card_number = phone_number[cad]
        self.set_Account_Number(card_number)
