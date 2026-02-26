balance =int(input("Account balance:"))
Withdrawal = int(input("Withdrawal amount:"))
status = input("Verification status (True / False):").lower().strip()
if status == "true":
    status = True
elif status == "false":
    status = False
else:
    print("Invalid input.")
if Withdrawal<=balance and status == True :
    print("Withdrawal successful")
else:
    print("Transaction denied")