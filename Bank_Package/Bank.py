from Bank_Package import Accountss
from typing import List

class Bank:
    __accounts :List[Accountss] = list()
    __a1 = Accountss.Accountss

    def register_New_Customer(self, first_Name:str, last_Name: str, age:int, phone_number:str, pin:str):
        self.age_verifier(age)
        self.check_Phone_Number(phone_number)
        p1 = self.__a1.set_Account(first_Name , last_Name , age , phone_number , pin)
        self.__accounts.append(p1)
        self.__a1.create_Account_Number(phone_number)

    def age_verifier(self, age):
        if age < 18:
            raise AttributeError("you are not qualified to use this platform")

    def check_Phone_Number(self, phone_Number):
        if len(phone_Number) != 11:
            raise AttributeError("invalid number")

    def deposit(self, account_number: str,  amount: int):
        for accountss in self.__accounts :
            if accountss.get_Card_number() == account_number:
                accountss.deposit(amount, account_number)
                break
        raise AttributeError("account does not exist")

    def check_Balance(self,account_number: str):
        for accountss in self.__accounts:
            if accountss.get_Card_number() == account_number:
                accountss.get_Card_number()
                break
        raise AttributeError("account does not exist")

    def withdrawal(self,account_number: str, pin: str,amount: int):
        for accountss in self.__accounts :
            if accountss.get_Card_number() == account_number:
                accountss.withdraw(pin , amount , account_number)
                break

        raise AttributeError("account does not exist")






