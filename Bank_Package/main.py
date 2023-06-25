from Bank_Package import Bank

b1 = Bank.Bank
if __name__ == '__main__' :

    def register_account() :
        first_name = input("input your first name")
        last_name = input("input your last name")
        age = int(input("input your age"))
        phone = input("enter phone number")
        pin = input("choose a pin")
        try :
            b1.register_New_Customer(first_name, last_name, age, phone, pin)
        except:
            print("invalid number")
            display_menu()


    def check_balance() :
        acc_number = input("enter your account number")
        try:
            print(f"your balance is {b1.check_Balance(acc_number) }")
            display_menu()
        except:
            print("invalid account number")
            display_menu()




    def display_menu():
        choice_str = input("""
        welcome to David's Bank
        how may we help you today?
        1-> register account
        2-> check balance
        3-> withdraw 
        4-> get account number
        5-> transfer
        6-> deposit
        7-> exit
        """)
        choice = choice_str[0]
        if choice == '1' :
            register_account()
        elif choice == '2' :
            check_balance()
