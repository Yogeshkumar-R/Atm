from user import user, notes
class withdraw:
    def Withdraw(self):
        amount = int(input("Enter the Amount to Withdraw:"))
        original_withdraw_amount = amount
        if amount > user['balance']:
            print("Insufficient Fund Balance")
            return

        for note, count in notes.items():
            if amount >= note and count > 0:
                print(f"{note} * {amount // note} = {(note * (amount // note))}")
                notes[note] -= amount // note
                amount -= (amount // note) * note

        if amount == 0:
            user['balance'] -= original_withdraw_amount
            print(f"{original_withdraw_amount} is withdrawn")

