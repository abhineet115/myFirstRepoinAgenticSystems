name =str(input("Enter your name:"))
current_age =float(input("Enter your age:"))
age = int(current_age)
active_user =int(input("If you are Active user press 1 or Not then press 0:"))
if active_user == 1:
        active_user =True
else :active_user = False
print(f"User {name} is {age} years old. Active status: {active_user}")