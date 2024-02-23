from withdraw import withdraw
from deposit import deposit
from balance import balance
from user import user


if __name__ == "__main__":
    print("------------Welcome to ABC Banking------------")
    PIN = int(input("PIN:"))
    withdraw=withdraw()
    deposit=deposit()
    balance=balance()
    while True:
        if not PIN == user['pin']:
            raise ValueError("Invalid PIN")
        Action = int(input("Enter \n1-Deposit \n2-Withdraw \n3-Balance Enquiry \n4-Exit\n"))
        if Action == 1:
            deposit.Deposit()
        elif Action == 2:
            withdraw.Withdraw()
        elif Action == 3:
            balance.Balance_Enquiry()
        elif Action == 4:
            exit()
        else:
            print("Enter a VALID ENTRY!!!")
