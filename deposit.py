from user import user,notes

class deposit:
   def Deposit(self):
        denomination = int(input("Enter the Deposit Amount: "))
        if denomination <= 0:
            print("Incorrect deposit amount")
        two_thousand = int(input("no.of.2000: "))
        notes[2000]+=two_thousand
        five_hundred = int(input("no.of.500: "))
        notes[500] += five_hundred
        two_hundred = int(input("no.of.200: "))
        notes[200] += two_hundred
        hundred = int(input("no.of.100: "))
        notes[100] += hundred
        if two_thousand <= 0 or five_hundred <= 0 or two_hundred <= 0 or hundred <= 0 or denomination<=0:
            print("Deposit amount cannot be zero")
        two_thousand *= 2000
        five_hundred *= 500
        two_hundred *= 200
        hundred *= 100
        deposit_amount = two_thousand + five_hundred + two_hundred + hundred
        if deposit_amount == denomination:
            user['balance'] += denomination
            print("Your Deposit is Successful!!!")
            print(user['balance'])

        else:
            print("Deposit amount does not match with no of currency")
 
